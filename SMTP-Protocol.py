import socket
import base64
import ssl

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"


# Choose a mail server (e.g. Google mail server) and call it mailserver

# #Fill in start

mailserver = "smtp.gmail.com"

# #Fill in end


# Create socket called clientSocket and establish a TCP connection with mailserver

# Fill in start

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# establishes TCP connect with gmail mail server on port 587 smtp service
clientSocket.connect((mailserver, 587))

# Fill in end

# server response
recv = clientSocket.recv(1024).decode()
# print server response unless not 220, print message
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')


# Send HELO command and print server response.

heloCommand = 'EHLO gmail.com\r\n'

# send EHLO to google mail server to start the email process
clientSocket.send(heloCommand.encode())
# server response
recv1 = clientSocket.recv(1024).decode()
# print server response, if not 250, print message
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')


# Purpose: Informing google mail server packet to secure connection
# StartTls Query
startTlsCommand = 'STARTTLS\r\n'
# Send to google mail server
clientSocket.send(startTlsCommand.encode())
# response from google mail server
tls_recv = clientSocket.recv(1024).decode()
# print response
print (tls_recv)
# print response, if not 220, print message
if tls_recv[:3] != '220':
	print('220 reply not received from server')


# upgrade from an insecure connection to a secure one using ssl
ssl_clientSocket = ssl.wrap_socket(clientSocket)

# senders and recievers email
email =  "jeffdoe448@gmail.com"
# senders password
password = "jeff123ece!"

# converts email and password into base64
base64_str = ("\x00"+email+"\x00"+password).encode()
base64_str = base64.b64encode(base64_str)
# authentication for username and password to send mail
authMsg = "AUTH PLAIN ".encode()+base64_str+"\r\n".encode()
# sent on secure connection
ssl_clientSocket.send(authMsg)
# response message
recv_auth = ssl_clientSocket.recv(1024).decode()
# print but if the first 3 digits are not 250, print message
print(recv_auth)
if recv1[:3] != '250':
    print('250 reply not received from server.')


# Send MAIL FROM command and print server response.

# Fill in start
# the email for mail sender
fromCommand = "Mail FROM: <jeffdoe448@gmail.com> \r\n"
# send through secure connection
ssl_clientSocket.send(fromCommand.encode())
# response message
recv2 = ssl_clientSocket.read(1024).decode()
# print, but if the first 3 digits are not 250, print message
print(recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.')

# Fill in end



# Send RCPT TO command and print server response.

# Fill in start
# recipient of the email
rcp = "RCPT TO: <jeffdoe448@gmail.com> \r\n"
# sent through secure connection
ssl_clientSocket.write(rcp.encode())
# server response
recv3 = ssl_clientSocket.read(1024).decode()
# print but if the first three digits are not 250, print message
print(recv3)
if recv3[:3] != '250':
    print('250 reply not recieved from server')

# Fill in end



# Send DATA command and print server response.

# Fill in start

# defines the following information as the data of the email
dataCmd = 'DATA\r\n'
# sent through a secure connection
ssl_clientSocket.send(dataCmd.encode())
# server response
rec4 = ssl_clientSocket.read(1024).decode()
# print result but if the first 3 digits are not 354, print message
print(rec4)
if rec4[:3] != '354':
    print('354 reply not recieved from server')

# Fill in end

# Send message data.

# Fill in start
# sending the bulk of the email
ssl_clientSocket.write(msg.encode())
# Fill in end


# Message ends with a single period.
# Fill in start
# sending a period at the end of the email
ssl_clientSocket.write(endmsg.encode())
# Fill in end


# Send QUIT command and get server response.

# Fill in start
# ends SMTP processing
quit = 'QUIT \r\n'
# send through a secure connection
ssl_clientSocket.send(quit.encode())
# server response
recv5 = ssl_clientSocket.read(1024).decode()
# print response
print(recv5)
# if the first 3 digits are not 250, print message

if recv5[:3] != '250':
    print('250 reply not received from server')
# Fill in end
