# EmergencySMS
# Python 3.7
# 1.29.2019 TimRCM
# Purpose: Pull down a simple contact list and send each number an SMS for emergency situations 
# Utilizes Twilio's API 

from twilio.rest import Client

import config


client = Client(config.account_sid, config.auth_token)

for contact in config.userList:
    name = contact[0]
    number = contact[1]

    print(f'Messaging {name} at {number}...')
    
    message = client.messages \
        .create (
            body = 'The office will NOT be closed today.',
            from_= config.outbound_number,
            to = number
        )
    
    print(message.sid)


