# EmergencySMS
# Python 3.7
# 1.29.2019 TimRCM
# Purpose: Pull down a simple contact list and send each number an SMS for emergency situations 
# Utilizes Twilio's API 

from twilio.rest import Client

import config
import smtp

log = open('status.log', 'w')

client = Client(config.account_sid, config.auth_token)

for contact in config.userList:
    try:
        name = contact[0]
        number = contact[1]

        print(f'Messaging {name} at {number}...')
        
        message = client.messages \
            .create (
                body = config.body,
                from_= config.outbound_number,
                to = number
            )
        
        log.write(f'SUCCESS - Message ID {message.sid} sent to {name} at {number}\n\n')
    
    except:
        log.write(f'FAILURE - Unable to message {name} at {number}\n\n')

log.close()
smtp.send()
