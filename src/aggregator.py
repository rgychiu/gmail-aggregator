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
    # TODO: allow for manual addition of accounts rather than predefining and for looping for greater user experience
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

        # Fetch API constants and credentials from config
        api_user = manager.get_api_user()
        unread_label = manager.get_unread_label()
        filter_labels = set(manager.get_labels())
        
        acct_payload = manager.get_acct_messages()
        payload_labels = manager.get_payload_labels()
        payload_data = manager.get_payload()
        payload_headers = manager.get_payload_headers()

        # Call the Gmail API, retrieve important emails from each account
        service = build('gmail', 'v1', credentials=oauth_creds)
        messages = service.users().messages().list(userId=api_user).execute()
        for msg in messages.get(acct_payload):
            # for each message, get the associated labels to check if its unread and important
            msg_data = service.users().messages().get(userId=api_user, id=msg.get('id')).execute()
            msg_labels = set(msg_data.get(payload_labels))
            if unread_label in msg_labels and len(msg_labels.intersection(filter_labels)):
                print(msg_data.get(payload_data).get(payload_headers))
        # print(result.get(payload_labels), result.get(payload_data).get(payload_headers))

if __name__ == "__main__":
    main()
