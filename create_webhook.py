#! /usr/bin/env python3

import json
from lib import call_api


response = call_api(
    "https://api.launchpad.net/devel/~imagebuild/+livefs/ubuntu/bionic/ubuntu-cpc",
    method="post",
    data={
        "ws.op": "newWebhook",
        "delivery_url": "https://design.staging.ubuntu.com/?image.build",
        "event_types": ["livefs:build:0.1"],
    },
)
webhook = call_api(response.headers["Location"])

print(json.dumps(webhook.json(), indent=4, sort_keys=True))
