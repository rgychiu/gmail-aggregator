import os
import json

from core.Singleton import Singleton

CONFIG_PATH = "config.json"

# OAuth keys
ACCOUNT_DATA_KEY = "accounts"
CRED_DIR_KEY = "cred_rel_path"
TOKEN_DIR_KEY = "token_rel_path"
AUTH_EXT_KEY = "flow_ext"
SCOPE_KEY = "scopes"

# API keys
API_DATA_KEY = "api"
USER_KEY = "user_id"
UNREAD_KEY = "unread_label"
EXTRA_KEY = "ext_labels"

# Message keys
MESSAGE_KEY = "acct_payload"
PAYLOAD_KEY = "message_data"
PAYLOAD_LABELS_KEY = "message_labels"
PAYLOAD_HEADERS_KEY = "message_headers"


class ConfigManager(Singleton):
    def __init__(self):
        super().__init__
        with open(CONFIG_PATH, "r") as config_file:
            self.config = json.load(config_file)
    
    def get_cred_dir(self):
        return self.config[ACCOUNT_DATA_KEY][CRED_DIR_KEY]
    
    def get_token_dir(self):
        return self.config[ACCOUNT_DATA_KEY][TOKEN_DIR_KEY]

    def get_all_creds(self):
        user_dir = self.get_cred_dir()
        return os.listdir(user_dir)
        # acct_dir = self.config[CRED_DIR_KEY]
        # acct_files = os.listdir(acct_dir)
        # users = []
        # for acct in acct_files:
        #     with open(acct_dir + "/" + acct, "r") as curr_acct:
        #         users.append(json.load(curr_acct))
        # return users

    def get_auth_ext(self):
        return self.config[ACCOUNT_DATA_KEY][AUTH_EXT_KEY]

    def get_scopes(self):
        return self.config[ACCOUNT_DATA_KEY][SCOPE_KEY]

    def get_acct_messages(self):
        return self.config[API_DATA_KEY][MESSAGE_KEY]

    def get_api_user(self):
        return self.config[API_DATA_KEY][USER_KEY]

    def get_unread_label(self):
        return self.config[API_DATA_KEY][UNREAD_KEY]
    
    def get_labels(self):
        return self.config[API_DATA_KEY][EXTRA_KEY]

    def get_payload(self):
        return self.config[API_DATA_KEY][PAYLOAD_KEY]

    def get_payload_labels(self):
        return self.config[API_DATA_KEY][PAYLOAD_LABELS_KEY]

    def get_payload_headers(self):
        return self.config[API_DATA_KEY][PAYLOAD_HEADERS_KEY] 
