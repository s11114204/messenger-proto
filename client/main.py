import socket

HOST = "192.168.35.142"
PORT = 65432

print("Client launched.")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Connecting to: " + HOST + ":" + str(PORT))
    s.connect((HOST, PORT))
    s.sendall(b"Hello")

    msg = ""
    while True:
        msg = input()

        if msg == "finish":
            break

        send_data = str.encode(msg)
        s.sendall(send_data)

        receive_data = s.recv(1024)
        print(f"Received: {receive_data!r}")

    print("Closing connection")