import socket
import io
import shutil
import requests
import json

key = input("Be sure to run this as root/sudo. Press enter to continue.")
webhook = input("Paste your slack webhook url: ")
filename = "slacknotif"

with io.FileIO("%s" % filename, "w") as file:
    file.write(script)
shutil.move("./slacknotif", "/opt/%s" % filename)

def post_to_slack():
    slack_username = socket.gethostname()
    slack_message = print("Test.")
    slack_url = webhook
    payload = {'username:' : 'slack_username', 'text' : "slack_message"}
    r = requests.get('%s' % webhook, params=payload)

post_to_slack()