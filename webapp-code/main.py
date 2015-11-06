from google.appengine.api import users

import webapp2
import jinja2
import httplib2
import os
import sys
from datetime import datetime
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
MAIN_PAGE_HTML = """\
<html>
  <body>
    <form action="/cash">
      <div><input type="submit" value="Enter WebApp!"></div>
    </form>
  </body>
</html>
"""


#anyone that utilizes application needs to have encoder set up with youtube account, select webcam upon car to be the source
class MainPage(webapp2.RequestHandler):

    def get(self):
        # [START get_current_user]
        # Checks for active Google account session
        user = users.get_current_user()
        # [END get_current_user]

        # [START if_user]
        if user:

            self.response.headers['Content-Type'] = 'text/html; charset=utf-8'     
            self.response.write('Hello, ' + user.nickname() + '\n' + 
                """
                Instructions for setting up for use of application:
                1) Enable Youtube Live Streaming and download encoder
                2) Set up encoder with webcam on chassis
                After this is done, you are ready to use the application, select button to continue!
                """)
            self.response.write(MAIN_PAGE_HTML)
        else:
            self.redirect(users.create_login_url(self.request.uri))
        # [END if_not_user]
class WebApp(webapp2.RequestHandler):
    def get(self):
                # The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
                # the OAuth 2.0 information for this application, including its client_id and
                # client_secret. You can acquire an OAuth 2.0 client ID and client secret from
                # the Google Developers Console at
                # https://console.developers.google.com/.
                # Please ensure that you have enabled the YouTube Data API for your project.
                # For more information about using OAuth2 to access the YouTube Data API, see:
                #   https://developers.google.com/youtube/v3/guides/authentication
                # For more information about the client_secrets.json file format, see:
                #   https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
                CLIENT_SECRETS_FILE = """
                client_secret_426444730659-jn90ig2a7l3qiemrgt5d9ci3mg9q239k.apps.googleusercontent.com.json"
                """
                # This OAuth 2.0 access scope allows for full read/write access to the
                # authenticated user's account.
                YOUTUBE_READ_WRITE_SCOPE = "https://www.googleapis.com/auth/youtube"
                YOUTUBE_API_SERVICE_NAME = "youtube"
                YOUTUBE_API_VERSION = "v3"
                
                # This variable defines a message to display if the CLIENT_SECRETS_FILE is
                # missing.
                MISSING_CLIENT_SECRETS_MESSAGE = """
                WARNING: Please configure OAuth 2.0
                
                To make this sample run you will need to populate the client_secrets.json file
                found at:
                
                   %s
                
                with information from the Developers Console
                https://console.developers.google.com/
                
                For more information about the client_secrets.json file format, please visit:
                https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
                """% os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                   CLIENT_SECRETS_FILE))
                
                def get_authenticated_service(args):
                  flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
                    scope=YOUTUBE_READ_WRITE_SCOPE,
                    message=MISSING_CLIENT_SECRETS_MESSAGE)
                
                  storage = Storage("%s-oauth2.json" % sys.argv[0])
                  credentials = storage.get()
                
                  if credentials is None or credentials.invalid:
                    credentials = run_flow(flow, storage, args)
                
                  return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    http=credentials.authorize(httplib2.Http()))
                
                # Create a liveBroadcast resource and set its title, scheduled start time,
                # scheduled end time, and privacy status.
                def insert_broadcast(youtube, options):
                  insert_broadcast_response = youtube.liveBroadcasts().insert(
                    part="snippet,status",
                    body=dict(
                      snippet=dict(
                        title="cheese"
                        scheduledStartTime=datetime.now().time()
                      ),
                      status=dict(
                        privacyStatus="private"
                      )
                    )
                  ).execute()
                
                  snippet = insert_broadcast_response["snippet"]
                
                  print "Broadcast '%s' with title '%s' was published at '%s'." % (
                    insert_broadcast_response["id"], snippet["title"], snippet["publishedAt"])
                  return insert_broadcast_response["id"]
                
                # Create a liveStream resource and set its title, format, and ingestion type.
                # This resource describes the content that you are transmitting to YouTube.
                def insert_stream(youtube, options):
                  insert_stream_response = youtube.liveStreams().insert(
                    part="snippet,cdn",
                    body=dict(
                      snippet=dict(
                        title="cheese"
                      ),
                      cdn=dict(
                        format="1080p",
                        ingestionType="rtmp"
                      )
                    )
                  ).execute()
                
                  snippet = insert_stream_response["snippet"]
                
                  print "Stream '%s' with title '%s' was inserted." % (
                    insert_stream_response["id"], snippet["title"])
                  return insert_stream_response["id"]
                
                # Bind the broadcast to the video stream. By doing so, you link the video that
                # you will transmit to YouTube to the broadcast that the video is for.
                def bind_broadcast(youtube, broadcast_id, stream_id):
                  bind_broadcast_response = youtube.liveBroadcasts().bind(
                    part="id,contentDetails",
                    id=broadcast_id,
                    streamId=stream_id
                  ).execute()
                
                  print "Broadcast '%s' was bound to stream '%s'." % (
                    bind_broadcast_response["id"],
                    bind_broadcast_response["contentDetails"]["boundStreamId"])
                
                if __name__ == "__main__":
                  argparser.add_argument("--broadcast-title", help="Broadcast title",
                    default="New Broadcast")
                  argparser.add_argument("--privacy-status", help="Broadcast privacy status",
                    default="private")
                  argparser.add_argument("--start-time", help="Scheduled start time",
                    default='2014-01-30T00:00:00.000Z')
                  argparser.add_argument("--end-time", help="Scheduled end time",
                    default='2014-01-31T00:00:00.000Z')
                  argparser.add_argument("--stream-title", help="Stream title",
                    default="New Stream")
                  args = argparser.parse_args()
                
                  youtube = get_authenticated_service(args)
                  try:
                    broadcast_id = insert_broadcast(youtube, args)
                    stream_id = insert_stream(youtube, args)
                    bind_broadcast(youtube, broadcast_id, stream_id)
                  except HttpError, e:
                    print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
                JINJA_ENVIRONMENT.get_template('iframe.html').render()


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/cash', WebApp)
], debug=True)