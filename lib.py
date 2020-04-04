import requests
import os


def call_api(url, method="get", data=None):
    return requests.request(
        method=method,
        url=url,
        headers={
            "Accept": "application/json",
            "Authorization": (
                f'OAuth oauth_version="1.0", '
                f'oauth_signature_method="PLAINTEXT", '
                f"oauth_consumer_key=image.build, "
                f'oauth_token="{os.environ["IMAGEBUILD_OAUTH_TOKEN"]}", '
                f'oauth_signature="{os.environ["IMAGEBUILD_OAUTH_SIGNATURE"]}"'
            ),
        },
        data=data,
    )
