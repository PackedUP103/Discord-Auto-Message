#modules#
import requests
import os
import time
import datetime

while True:
  if datetime.datetime.now().hour % 2 == 0: # Set time ammount (hour , minute , second) change "2" to number of time to send
    payload = {
      'content': "MESSAGE" # Message #
    }

    header = {
      'authorization': 'TOKEN' # Account Token #
    }
    
    r = requests.post("https://discord.com/api/v8/channels/ID/messages", data=payload, headers=header) # Replace ID in string to your channel ID to send the messages in, do not change string only ID
    time.sleep(60) # Dont change this

# Script will repeat

# Script Version : 1.0
# By : PackedUP

