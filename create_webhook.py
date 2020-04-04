from lib import call_api


response = call_api(
    "https://api.launchpad.net/devel/~imagebuild/+livefs/ubuntu/bionic/ubuntu-core",
    method="post",
    data={
        "ws.op": "newWebhook",
        "delivery_url": "http://demo.haus:8000/",
        "event_types": ["livefs:build:0.1"],
    },
)
webhook = call_api(response.headers["Location"])

print(json.dumps(webhook.json(), indent=4, sort_keys=True))
