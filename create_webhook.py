from lib import call_api


webhook_response = call_api(
    "https://api.launchpad.net/devel/~imagebuild/+livefs/ubuntu/bionic/ubuntu-core",
    method="post",
    data={
        "ws.op": "newWebhook",
        "delivery_url": "http://demo.haus:8000/",
        "event_types": ["livefs:build:0.1"],
    },
)
