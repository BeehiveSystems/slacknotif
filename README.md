# slacknotif
A python-based slack notifier for linux systems. 

The port from https://github.com/lohayon5/slack_notif/ is complete. Functionality is still limited to cron updates, though you may edit the script as needed.

Yum and apt systems are now supported. 

Current usage: 

-Run slacknotif.py as sudo/root.  
-Enter your Slack webhook url.  
-Call slacknotif with ```echo "Hello World!" | /opt/slacknotif```  
-Slacknotif will send you a message on Slack with "Hello World!" as its content.  
-Select whether you have a RHEL or Debian based system.  

More to come soon.
