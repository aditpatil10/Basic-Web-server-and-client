
# Import socket module
import socket
# Import thread module
import threading


url1 = "http://localhost:8080/index.html"
url2 = "http://localhost:8080/"         # URLS for request and comparison
# Create a TCP server socket


serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Assign a port number
serverPort = 8080


# Bind the socket to server address and server port

serverSocket.bind((socket.gethostname(), serverPort))

# Listen to at most 5 connection at a time

serverSocket.listen(5)

# Server should be up and running and listening to the incoming connections


def multi_thread(connectionSocket):
    if clienturl == url1 or clienturl == url2 or clienturl == url3:
        # Extracting the path of the requested object from the message
        clientsocket.send(bytes("HTTP/1.1 200 OK", "UTF-8"))
        filename = 'index.html'  # sending web page to client
        f = open(filename, 'rb')
        l = f.read(1024)
        while (l):
            clientsocket.send(l)
            print('S: Sent data to client sucessfully ')
            l = f.read(1024)
        f.close()  # closing socket
        clientsocket.close()  # closing socket
    else:
        print(f'S: Failed to connect with client with address {address} ')
        # sending failure header to client
        clientsocket.send(bytes("HTTP/1.1 404 Not Found", "UTF-8"))
        clientsocket.close()  # closing socket


while True:
    clientsocket, address = serverSocket.accept()
    print(
        f"S: Connection Successful! Connected to client with address {address}")
    msg = clientsocket.recv(1024)       # receiving message from client
    clienturl = msg.decode("UTF-8")
    # creating the thread for every client
    t = threading.Thread(target=multi_thread, name='t', args=(clienturl,))
    t.start()
