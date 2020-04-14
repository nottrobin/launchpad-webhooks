#! /usr/bin/env python3

import json
from lib import call_api


deliveries_response = call_api(
    "https://api.launchpad.net/devel/~imagebuild/+livefs/ubuntu/bionic/ubuntu-core/+webhook/12811/deliveries"
)

print(json.dumps(deliveries_response.json(), indent=4, sort_keys=True))
