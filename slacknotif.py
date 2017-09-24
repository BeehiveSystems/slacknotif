#!/usr/bin/env python3
import io
import shutil

key = input("Be sure to run this as root/sudo. Press enter to continue.")
webhook = input("Paste your slack webhook url: ").encode()
filename = "slacknotif"

with io.FileIO("%s" % filename, "w") as file:
    file.write(
"""#!/usr/bin/env python3
import socket
import io
import requests
import json
import sys

def post_to_slack():
    slack_message = "".join(sys.stdin)
    slack_username = socket.gethostname()
    payload = {'username': slack_username, 'text': slack_message,}
    requests.post("%s", json=payload)
post_to_slack()""".encode() % webhook)

shutil.move("./slacknotif", "/opt/%s" % filename)