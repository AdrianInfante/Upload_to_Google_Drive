import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from datetime import datetime

# Path to the credentials JSON file you downloaded
credentials_path = r'yourGoogleCredentials.json'

# Replace with the desired file to upload
file_path = r'yourfilepath'


# ID of the shared folder where you want to upload the file
folder_id = 'folder_shared_ID'

# Authenticate with Google Drive API 
creds = service_account.Credentials.from_service_account_file(credentials_path, scopes=['https://www.googleapis.com/auth/drive'])
drive_service = build('drive', 'v3', credentials=creds)

# Create a folder with the current date and time as the folder name
now = datetime.now()
folder_name = now.strftime("%Y-%m-%d %H:%M:%S")
folder_metadata = {
    'name': folder_name,
    'mimeType': 'application/vnd.google-apps.folder',
    'parents': [folder_id]  # Specify the parent folder ID here
}
folder = drive_service.files().create(body=folder_metadata, fields='id').execute()
folder_id = folder.get('id')

# Create a file metadata with the specified folder ID
file_metadata = {
    'name': os.path.basename(file_path),
    'parents': [folder_id]
}

# Upload the file
media = MediaFileUpload(file_path, mimetype='application/octet-stream')
file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()

print(f'File ID: {file.get("id")}')


