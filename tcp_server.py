
import socket 
  
# Defining Socket 
host = '127.0.0.1'
port = 8888
totalclient = int(input('Enter number of clients: ')) 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sock.bind((host, port)) 
sock.listen(totalclient) 
# Establishing Connections 
connections = [] 
print('Initiating clients') 
for i in range(totalclient): 
    conn, addr = sock.accept() 
    connections.append(conn) 
    print('Connected with client', i+1) 

fileno = 0
for idx, conn in enumerate(connections, 1): 
    # Receiving File Data 
    data = conn.recv(1024)
    if not data:
        continue
    # Creating a new file at server end and writing the data 
    filename = 'output' + str(fileno) + '.txt'
    fileno += 1
    with open(filename, "wb") as fo:
        fo.write(data) 

    print() 
    print('Receiving file from client', idx) 
    print() 
    print('Received successfully! New filename is:', filename) 

# Closing all Connections 
for conn in connections: 
    conn.close() 
