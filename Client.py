import socket

def start_client():
    host = '192.168.1.13'
    port = 5555

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    while True:
        message = input("Masukkan pesan (ketik 'exit' untuk keluar): ")
        client.send(message.encode('utf-8'))

        if message.lower() == 'exit':
            break

        response = client.recv(1024).decode('utf-8')
        print(f"Response dari server: {response}")

    client.close()

if __name__ == "__main__":
    start_client()
