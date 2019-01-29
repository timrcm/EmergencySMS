# Account SID & auth token from twilio.com/console
account_sid = ''
auth_token = ''
outbound_number = '+1'

# Message to send
body = 'SMS Spam'

# User list - import this from a CSV later?
userList = [
    ('Bob Dole', '+15556667777'),
    ('Joe Smith', '+16667778888'),
    ('Sally Sals', '+17778889999')
]

# SMTP config

smtp_sendfrom = ''
smtp_sendto = ''
smtp_host = '1.2.3.4'
smtp_port = 25
smtp_auth_req = 0 # Set to '1' if authentication is required
smtp_username = ''
smtp_password = ''
