# Adit Patil
# ID:1001757372


import socket  # for socket connection
import os  # for renaming files
import random  # python library for genrating random numbers
import webbrowser  # for opening webpages


url = input()  # take the url from the user

# creating client socket
csocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
csocket.connect((socket.gethostname(), 8080))   # connect to the server


csocket.send(bytes(url, "UTF-8"))  # sending data to server


msg = csocket.recv(1024)  # receiving message from client
# decoding the message which was encoded by the server
message = msg.decode("UTF-8")
print("C: ", message)
# Checking the message from server basically giving the green signal
check = "HTTP/1.1 200 OK"
if message == check:
    num = random.randint(1, 100)  # creating a random number for file
    msg = csocket.recv(1024)  # receiving message from server
    filecontent = msg.decode("UTF-8")  # decoding the message
    f = open("index%s.txt" % num, 'w')
    f.write(filecontent)    # writing contents in the text file
    f.close()
    os.rename("index%s.txt" % num, "index%s.html" %
              num)  # renaming text file to html file
    webbrowser.open("index%s.html" % num, new=2)  # opening in new tab
    csocket.close()
else:
    csocket.close()
