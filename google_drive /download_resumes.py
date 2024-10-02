import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload 
from google.oauth2.credentials import Credentials

RESUMES_FOLDER = './resumes'
SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]


credentials = Credentials.from_authorized_user_file('token.json', SCOPES)

service = build('drive', 'v3', credentials=credentials)

folder_id = '1sJSp5VvE58lPq_tD5t3H5RMRYV56z_ie'

# Return a dict with ID and Name for each resume in the folder_id 
results = service.files().list(
    q=f"'{folder_id}' in parents", fields="files(id, name)"
).execute()
print(results)

# Get list of files. If 'files' doesnt exist, return a []
files = results.get('files', [])
print(files)

if not os.path.exists(RESUMES_FOLDER):
    os.makedirs(RESUMES_FOLDER)

if not files: 
    raise FileNotFoundError('No files found')
else: 
    print('Files: ')
    for file in files: 
        print(f"{file['name']} ({file['id']})")
        # Donwload each file from drive by its ID
        request = service.files().get_media(fileId=file['id'])
        file_path = f"{RESUMES_FOLDER}/{file['name']}"
        with open(file_path, 'wb') as f: 
            downloader = MediaIoBaseDownload(f, request)
            done = False 
            while not done:
                # Get a tuple from the downloader object.  
                status, done = downloader.next_chunk()
                print(f"Download {int(status.progress() * 100)}%.")

