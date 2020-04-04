import json
from lib import call_api


webhooks_response = call_api(
    "https://api.launchpad.net/devel/~imagebuild/+livefs/ubuntu/bionic/ubuntu-core/webhooks"
)

print(json.dumps(webhooks_response.json(), indent=4, sort_keys=True))
