import socket
import threading

# Ubah alamat broadcast sesuai dengan subnet jaringan Anda
BROADCAST_IP = "192.168.1.255"  # Sesuaikan dengan alamat broadcast jaringan
PORT = 12345
USERNAME = input("Masukkan nama pengguna: ")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.bind(("", PORT))

def receive_messages():
    while True:
        try:
            message, address = sock.recvfrom(1024)
            print(message.decode("utf-8"))
        except:
            break

def send_messages():
    while True:
        message = input("")
        full_message = f"{USERNAME}: {message}"
        sock.sendto(full_message.encode("utf-8"), (BROADCAST_IP, PORT))

threading.Thread(target=receive_messages, daemon=True).start()
send_messages()
