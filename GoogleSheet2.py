

from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run
from oauth2client.file import Storage

CLIENT_ID = '<Client ID from Google API Console>'
CLIENT_SECRET = '<Client secret from Google API Console>'

flow = OAuth2WebServerFlow(
          client_id = "117800781162851201760",
          client_secret = CLIENT_SECRET,
          scope = 'https://spreadsheets.google.com/feeds https://docs.google.com/feeds',
          redirect_uri = 'http://example.com/auth_return'
       )

storage = Storage('creds.data')
credentials = run(flow, storage)
print "access_token: %s" % credentials.access_token
