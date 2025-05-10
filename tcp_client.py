import socket 

host = '127.0.0.1'
port = 8888
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# Connecting with Server 
sock.connect((host, port)) 

while True: 
    filename = input('Input filename you want to send: ') 
    try: 
        # Reading file and sending data to server 
        with open(filename, "rb") as fi: 
            data = fi.read() 
            if not data: 
                break
            sock.sendall(data)
            print("File sent successfully!")
            break  # Assuming one file transfer per client connection

    except FileNotFoundError: 
        print('File not found! Please enter a valid filename') 
    except Exception as e:
        print("Error:", e)
    finally:
        sock.close()
