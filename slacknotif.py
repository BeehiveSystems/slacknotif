import io
import shutil

print("Be sure to run this as sudo/root. Press enter to continue...")

url = input("Paste your slack webhook url: ")
filename = "slacknotif"
script = """#!/bin/bash
	function post_to_slack () {
	       	SLACK_USERNAME="$(hostname)"
 	     	SLACK_MESSAGE="$1"
     		SLACK_URL=$SLACK_URL
	        curl -sSL --data "payload={\"username\": \"${SLACK_USERNAME}\", \"text\": \"${SLACK_ICON} ${SLACK_MESSAGE}\"}" ${SLACK_URL}
	}
	post_to_slack "$(cat)"
	exit 0""".encode()

with io.FileIO("slacknotif", "w") as file:
    file.write(script)

shutil.move("./slacknotif", "/opt/%s" % filename)