import pickle
import os.path
import json

from core.ConfigManager import ConfigManager
from utils.utils import get_alias

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    manager = ConfigManager()
    cred_dir = manager.get_cred_dir()
    token_dir = manager.get_token_dir()
    token_ext = manager.get_auth_ext()

    users = manager.get_all_creds()
    scopes = manager.get_scopes()

    # complete authorization flow for all accounts
    for account in users:
        oauth_creds = None
        oauth_session_file = get_alias(cred_dir, account) + token_ext

        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(token_dir + "/" + oauth_session_file):
            with open(token_dir + "/" + oauth_session_file, "rb") as token:
                oauth_creds = pickle.load(token)

        # If there are no (valid) credentials available, let the user log in.
        if not oauth_creds or not oauth_creds.valid:
            if oauth_creds and oauth_creds.expired and oauth_creds.refresh_token:
                oauth_creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(cred_dir + "/" + account, scopes)
                oauth_creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(token_dir + "/" + oauth_session_file, "wb") as token:
                pickle.dump(oauth_creds, token)

    # service = build('gmail', 'v1', credentials=creds)

    # # Call the Gmail API
    # results = service.users().labels().list(userId='me').execute()
    # labels = results.get('labels', [])

    # if not labels:
    #     print('No labels found.')
    # else:
    #     print('Labels:')
    #     for label in labels:
    #         print(label['name'])


if __name__ == "__main__":
    main()
