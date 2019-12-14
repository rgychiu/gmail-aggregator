import os
import json

from core.Singleton import Singleton

CONFIG_PATH = "config.json"

# OAuth keys
CRED_DIR_KEY = "cred_rel_path"
TOKEN_DIR_KEY = "token_rel_path"
AUTH_EXT_KEY = "flow_ext"
SCOPE_KEY = "scopes"


class ConfigManager(Singleton):
    def __init__(self):
        super().__init__
        with open(CONFIG_PATH, "r") as config_file:
            self.config = json.load(config_file)
    
    def get_cred_dir(self):
        return self.config[CRED_DIR_KEY]
    
    def get_token_dir(self):
        return self.config[TOKEN_DIR_KEY]

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
        return self.config[AUTH_EXT_KEY]

    def get_scopes(self):
        return self.config[SCOPE_KEY]
