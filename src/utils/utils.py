import json


def get_alias(cred_dir, cred_file):
    """Get account alias for a specific credentials file name."""
    with open(cred_dir + "/" + cred_file, "r") as f:
        account = json.load(f)
        return account["alias"]
