#! /usr/bin/env python3

import sys
from lib import call_api


system_type = sys.argv[1]
webhook_id = sys.argv[2]
url = (
    "https://api.launchpad.net/devel/~imagebuild/+livefs/"
    f"ubuntu/{system_type}/+webhook/{webhook_id}"
)

response = call_api(url, method="delete")

print(response)
