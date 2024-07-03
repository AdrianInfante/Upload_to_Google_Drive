# Google Drive API Upload Script

This Python script demonstrates how to authenticate with the Google Drive API using a service account and upload a file to a specific folder in Google Drive. The script also creates a new subfolder with the current date and time as its name within the specified parent folder, then uploads the file into this new subfolder.

## Prerequisites

1. **Google Cloud Platform Project**: You need a Google Cloud Platform project with the Google Drive API enabled.
2. **Service Account**: Create a service account for your project and download the credentials JSON file.
3. **Google Drive Folder**: Ensure you have the ID of the parent folder in Google Drive where you want to upload the file.

## Setup

1. **Install Required Libraries**:
   You need to install the `google-auth`, `google-auth-oauthlib`, and `google-api-python-client` libraries. You can install these using pip:

   ```sh
   pip install google-auth google-auth-oauthlib google-api-python-client
   ```

2. **Prepare Your Script**:
   Save your credentials JSON file and note down the path. Replace the `credentials_path`, `file_path`, and `folder_id` variables in the script with your actual values.


### Steps in the Script

1. **Import Libraries**: Import the necessary libraries for handling Google Drive API interactions, authentication, file uploads, and date/time operations.
2. **Define Paths and IDs**: Specify the paths to the credentials file and the file to upload, as well as the ID of the parent folder.
3. **Authenticate**: Use the service account credentials to authenticate with the Google Drive API.
4. **Create Subfolder**: Generate a new subfolder named with the current date and time under the specified parent folder.
5. **Upload File**: Upload the specified file to the newly created subfolder and print the file ID.

## Usage

1. **Edit the Script**: Replace the placeholder values with your actual paths and IDs.
2. **Run the Script**: Execute the script to upload your file to Google Drive.

```sh
python your_script.py
```

## Notes

- Make sure the service account has appropriate permissions to access and upload files to the specified Google Drive folder.
- The script uploads the file with an `application/octet-stream` MIME type. Adjust the MIME type as needed based on the file type you are uploading.

This README provides an overview of how to use the script to upload files to Google Drive using the Google Drive API.
