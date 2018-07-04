# Import smtplib to provide email functions
import smtplib

# Import the email modules
from email.mime.text import MIMEText

# Define file containing message for us to send
MSG_FILE = './test.msg'

# Define email addresses to use
# ADDR_TO   = 'david_bryant@yahoo.com'
ADDR_TO   = 'mtbryant742@gmail.com'
ADDR_FROM = 'wxinfo@orangemoose.com'

# Define SMTP email server detail
SMTP_SERVER = 'mail.orangemoose.com'
SMTP_USER   = 'wxinfo@orangemoose.com'
SMTP_PASS   = 'Xn3wHu4msaVQU8xNYBqP8'

# Construct email
f = open(MSG_FILE,'r')
msg = MIMEText(f.read())
msg['To'] = ADDR_TO
msg['From'] = ADDR_FROM
msg['Subject'] = 'System message from your friendly Wxinfo Bot (wxinfo@orangemoose.com)'


# General case: Send the message via an SMTP server
# s = smtplib.SMTP(SMTP_SERVER)
# s.login(SMTP_USER,SMTP_PASS)
# s.sendmail(ADDR_FROM, ADDR_TO, msg.as_string())


# Special SMTP sequence when sending via Google Mail (UNTESTED)
# s = smtplib.SMTP('smtp.gmail.com:587')
# s.ehlo_or_helo_if_needed()
# s.starttls()
# s.ehlo_or_helo_if_needed()
# s.login(SMTP_USER,SMTP_PASS)
# s.sendmail(ADDR_FROM, ADDR_TO, msg.as_string())

# SMTP sequence when sending via GMX or orangemoose.com (via Dreamhost)
try:
    s = smtplib.SMTP(SMTP_SERVER,587)
    s.set_debuglevel(1)
    s.ehlo_or_helo_if_needed()
    s.starttls()
    s.ehlo_or_helo_if_needed()
    s.login(SMTP_USER,SMTP_PASS)
    s.sendmail(ADDR_FROM, ADDR_TO, msg.as_string())
    # Close server connection
    s.quit()
    print "Successfully sent email"
except:
    print "Error: unable to send email"

