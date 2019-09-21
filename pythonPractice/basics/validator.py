#example ofcustom module
import re

def validate_email(email):
    if len(email) > 7:
        return bool(re.match("^.+@(\[?)[a-zA-z0-9-.]+.({a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email))