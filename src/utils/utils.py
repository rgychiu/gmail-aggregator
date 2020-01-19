import json

# TODO: finish docstrings
def get_alias(cred_dir, cred_file):
    """Get account alias for a specific credentials file name."""
    with open(cred_dir + "/" + cred_file, "r") as f:
        account = json.load(f)
        return account["alias"]


def get_metadata(headers):
    """Get relevant metadata of the email from corresponding message headers,
    including sender, recipient, date, and subject."""
    msg_data = dict()
    for header in headers:
        if header.get("name") is not None:
            curr_header = header.get("name").lower()
            curr_value = header.get("value")
            if curr_header == "from":
                msg_data["sender"] = curr_value
            elif curr_header == "to":
                msg_data["recipient"] = curr_value
            elif curr_header == "date":
                msg_data["date"] = curr_value
            elif curr_header == "subject":
                msg_data["subject"] = curr_value
    return msg_data
