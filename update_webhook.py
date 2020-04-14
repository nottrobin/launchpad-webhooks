#! /usr/bin/env python3

from lib import call_api


update_response = call_api(
    "https://api.launchpad.net/devel/~imagebuild/+livefs/ubuntu/bionic/ubuntu-core/+webhook/12811",
    method="patch",
    json={"delivery_url": "https://design.staging.ubuntu.com/?image.build"},
)

import ipdb

ipdb.set_trace()
