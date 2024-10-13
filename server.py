import socket
import sys

from faker import Factory

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind(("localhost", 12345))

    server_socket.listen(1)

    fake = Factory.create()

    try:
        while True:
            client_socket, client_address = server_socket.accept()

            print(f"connection from {client_address}")

            while True:
                data = client_socket.recv(4096)

                print(f"Received data: {data.decode()}")

                if data:
                    response = fake.text()
                    client_socket.sendall(response.encode())
                else:
                    print(f"no data from {client_address}")
                    break
    except KeyboardInterrupt:
        print("Shutting down server")
    except Exception as e:
        sys.stderr.write(f"An error occurred: {e}")
