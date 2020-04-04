from wsgiref.simple_server import make_server
import datetime
import json


def application(env, start_response):
    """
    A basic WSGI application
    """

    timestamp = datetime.datetime.now().isoformat()

    with open(f"events/{timestamp}.json", "w") as eventfile:
        newenv = env.copy()
        del newenv["wsgi.file_wrapper"]
        del newenv["wsgi.errors"]
        del newenv["wsgi.input"]
        json.dump(newenv, eventfile, indent=4, sort_keys=True)

    start_response(
        status="200 OK", headers=[("Content-Type", "application/json")]
    )

    return ["[]".encode("utf-8")]


if __name__ == "__main__":
    make_server("", 80, application).serve_forever()
