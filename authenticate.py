import os.path 
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Define Scopes to allow reading and modifying files on Google Drive
SCOPES = [
    "https://www.googleapis.com/auth/drive.file", # Actions 
    "https://www.googleapis.com/auth/drive.readonly", # Read  
    "https://www.googleapis.com/auth/drive.metadata.readonly" # Read metadada 
]

credentials = None 

# Check if token.json exists in the actual dir, since this file has the credentials. 
if os.path.exists('token.json'): 
    credentials = Credentials.from_authorized_user_file('token.json', SCOPES)
    print('Credentials loaded successfully!')

if not credentials or not credentials.valid: 
    if credentials and credentials.expired and credentials.refresh_token: 
        credentials.refresh(Request())
        print('Credentials renewed successfully!')
    else: 
        print('Initiliazing the authorization flow from OAuth..')
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        credentials = flow.run_local_server(port=0)
        print('Authentication concluded!')
    
    with open('token.json', 'w') as token:
        token.write(credentials.to_json())
        print('Credentials saved in token.json.')