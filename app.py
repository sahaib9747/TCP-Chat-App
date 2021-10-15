import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ipv4 and tcp

def server():
    port = 8000
    sock.bind(('', port))
    sock.listen(1)
    client, address = sock.accept()
    while True:
        try:
            message = client.recv(4096)
            print(f"Friend: {message.decode()}")

            if message.decode().lower() == 'bye':
                client.send("Bye my friend".encode())
                print('You: Bye my friend')
                client.close()
                sock.close()
                break
            client.send(input('You: ').encode())
        except (KeyboardInterrupt, ConnectionResetError):
            sock.send('bye'.encode())
            client.close()
            sock.close()


def client():
    host = 'localhost'
    port = 8000
    sock.connect((host, port))

    while True:
        try:
            sock.send(input('You: ').encode())
            message = sock.recv(4096)
            print(f'Friend: {message.decode()}')

            if 'bye' in message.decode().lower():
                sock.send('ok Bye'.encode())
                print('You: ok Bye')
                sock.close()
                break

        except (KeyboardInterrupt, ConnectionResetError):
            print('Exiting the conversation')

            sock.send(input('Bye my dear friend.').encode())
            sock.close()

   

if __name__ == '__main__':
    user = int(input("Select the option: Who you are ?\n1.Server\n2.Client\n> "))

    if user == 1:
        server()
    else:
        client()
