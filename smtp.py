import smtplib

import config

log = open('status.log', 'r')

headers = f"""From: Office Notifications <{config.smtp_sendfrom}>
To: <{config.smtp_sendto}>
Subject: Emergency SMS Sent
"""

def send():
    # Istantiate smtplib & log in if needed 
    # SMTP_SSL is used here -- allow configuration for insecure SMTP servers later?
    
    msg =  f"""{headers}
SMS message was sent out saying:

'{config.body}'

Log:

{log.read()}"""
    
    try: 
        notify = smtplib.SMTP(host=config.smtp_host, port=config.smtp_port)
        if config.smtp_auth_req == 1:
            notify.login(config.smtp_username, config.smtp_password)
        notify.sendmail(config.smtp_sendfrom, config.smtp_sendto, msg)
        print('Notification sent.')

    except:
        print('Failed to send notification.')
        exit(1)

# send('Test')