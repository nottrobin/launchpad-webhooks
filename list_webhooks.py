#! /usr/bin/env python3

import json
import sys
from lib import call_api


system_type = sys.argv[1]

webhooks_response = call_api(
    "https://api.launchpad.net/devel/~imagebuild/"
    f"+livefs/ubuntu/{system_type}/webhooks"
)

print(json.dumps(webhooks_response.json(), indent=4, sort_keys=True))
