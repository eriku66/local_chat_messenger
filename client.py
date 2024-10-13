import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ("localhost", 12345)

print(f"connecting to {server_address}")

try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

try:
    while True:
        input_str = input("Enter your message: ")

        sock.sendto(input_str.encode(), server_address)

        data = sock.recv(4096)

        if data:
            print(f"Server response: {data.decode()}")
        else:
            break
except (KeyboardInterrupt, EOFError):
    print("")
finally:
    print("closing socket")
    sock.close()
