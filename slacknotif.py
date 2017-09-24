import socket
import io
import shutil
import requests
import json

key = input("Be sure to run this as root/sudo. Press enter to continue.")
webhook = input("Paste your slack webhook url: ")
filename = "slacknotif"

def post_to_slack():
    slack_username = socket.gethostname()
    slack_message = "Test."
    payload = {'username': slack_username, 'text': slack_message,}
    requests.post(webhook, json=payload)
post_to_slack()

#Still need to add webhook in /opt/ file. 

with io.FileIO("%s" % filename, "w") as file:
    file.write("import socket\n".encode())
    file.write("import io\n".encode())
    file.write("import requests\n".encode())
    file.write("import json\n".encode())
    file.write("def post_to_slack():\n".encode())
    file.write("    slack_message = \"Test.\"\n".encode())
    file.write("    slack_username = socket.gethostname()\n".encode())
    file.write("    payload = {'username': slack_username, 'text': slack_message,}\n".encode())
    file.write("    requests.post(webhook, json=payload)\n".encode())
    file.write("post_to_slack()\n".encode())
shutil.move("./slacknotif", "/opt/%s" % filename)