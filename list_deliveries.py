#! /usr/bin/env python3

import json
import sys
from lib import call_api


system_type = sys.argv[1]
webhook_id = sys.argv[2]
url = (
    "https://api.launchpad.net/devel/~imagebuild/+livefs/"
    f"ubuntu/{system_type}/+webhook/{webhook_id}/deliveries"
)

deliveries_response = call_api(url)

print(json.dumps(deliveries_response.json(), indent=4, sort_keys=True))
