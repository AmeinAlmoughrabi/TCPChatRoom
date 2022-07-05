import smtplib
# protocol used to send mail
# takes script and logs into existing mailing account and using smtplib protocol with my script to send mail
from email import encoders
# used to encode the message
from email.mime.base import MIMEBase
# used for attaching files
from email.mime.multipart import MIMEMultipart
# used for entire email
from email.mime.text import MIMEText
# used for text email



server = smtplib.SMTP('smtp.gmail.com', 587)
# initializes server and port

# why 587?
# google uses this port to send mailm
# 587 is a standard port for SMTP

# start server by calling ehlo()
server.ehlo()

# read in credentials
with open('credentials.txt', 'r') as f:
    username = f.readline().strip()
    # reads the first line of the file and strips the newline character
    password = f.readline().strip()
    # reads the second line of the file and strips the newline character
    
    # reads in credentials from credentials.txt
    # strip() removes newline character

# what does credentials.txt look like?
# username
# password


# start TLS encryption
server.starttls()
# starttls() is a method that starts the TLS encryption
# it is a standard protocol for starting TLS encryption


server.login(username, password)
# login() is a method that logs into the server
# takes in username and password


# MIMEMultipart() is a class that creates a message
# MIMEBase() is a class that creates a file attachment
# MIMEText() is a class that creates a text email
# MIMEMultipart() is a class that creates a message

message = MIMEMultipart()
# define header of message
# message can be treated as a dictionary so therefore:
message['From'] = username
message['to'] = 'kerimkarabacak100@gmail.com'
message['subject'] = 'GG GET SENT TO THE LOBBY'

with open('message.txt', 'r') as f:
    message.attach(MIMEText(f.read(), 'plain'))
    # attach() is a method that attaches a file to the message
    # takes in a file and a type of file
    # type of file is plain text
    # plain text is the default type of file
    # attachs message.txt to message
    # message.txt is the file that contains the message
    # message.txt is the body of the email


message.attach(MIMEText('This is an attachment.', 'plain'))
# attach() is a method that attaches a file to the message
# takes in a file and a type of file
# type of file is plain text


filename = 'attachment.jpg'
attachment = open(filename, 'rb')
# reads in byte mode because it is image data

# create payload object
payload = MIMEBase('application', 'octet-stream')
# octet-stream is the default type of stream that processes image data
payload.set_payload((attachment).read())
# read content of attachment and set it to payload

# use encoders to encode the payload in base 64
encoders.encode_base64(payload)

payload.add_header('Content-Disposition', 'attachment', filename=filename)
message.attach(payload)

text = message.as_string()
# as_string() is a method that converts the message to a string

server.sendmail(username, '', text)

# Done!
