import socket
import threading

# Fungsi untuk menangani setiap koneksi klien
def handle_client(client_socket, addr):
    while True:
        # Menerima pesan dari klien
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        print(f"Pesan dari {addr[0]}: {data}")

        # Mengirim pesan kembali ke klien
        response = f"Pesan diterima: {data}"
        client_socket.send(response.encode('utf-8'))

    # Menutup koneksi ketika klien keluar dari loop
    print(f"Koneksi dengan {addr[0]} telah ditutup.")
    client_socket.close()

def start_server():
    host = '192.168.1.13'
    port = 5555

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)

    print(f"Server sedang mendengarkan di {host}:{port}")

    while True:
        client, addr = server.accept()
        print(f"Koneksi diterima dari {addr[0]}:{addr[1]}")

        # Memulai thread baru untuk menangani setiap koneksi klien
        client_handler = threading.Thread(target=handle_client, args=(client, addr))
        client_handler.start()

if __name__ == "__main__":
    start_server()
