import json
from lib import call_api


response = call_api(
    "https://api.launchpad.net/devel/~imagebuild/+livefs/ubuntu/bionic/ubuntu-core",
    method="post",
    data={
        "ws.op": "requestBuild",
        "pocket": "Updates",
        "archive": "https://api.launchpad.net/1.0/ubuntu/+archive/primary",
        "distro_arch_series": (
            "https://api.launchpad.net/1.0/ubuntu/bionic/armhf"
        ),
        "metadata_override": json.dumps(
            {"subarch": "raspi3", "extra_snaps": ["toto"]}
        ),
    },
)
