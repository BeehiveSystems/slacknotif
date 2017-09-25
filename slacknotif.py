#!/usr/bin/env python3
import io
import shutil
import os

key = input("Be sure to run this as root/sudo. Press enter to continue.")
webhook = input("Paste your slack webhook url: ").encode()
filename = "slacknotif"
system = input("Are you using a Debian or RHEL based system? ").lower()

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
os.chmod("/opt/%s" % filename, 0o755)

if system == "debian":
	print("Adding cron updates for apt.")
	with io.FileIO("/etc/cron.d/slack", "w") as file:
		file.write(
			"""SHELL=/bin/sh
			PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
			30 8 * * * root /usr/bin/apt-get update && /usr/bin/apt-get install unattended-upgrades | /opt/%(filename)""".encode())
elif system == "rhel":
	print("Adding cron updates for yum.")
	with io.FileIO("/etc/cron.d/slack", "w") as file:
		file.write( 
			"""SHELL=/bin/sh
			PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
			30 8 * * * root /usr/bin/yum update | /opt/%(filename)""".encode())
else:
	print("Unrecognized system type.")