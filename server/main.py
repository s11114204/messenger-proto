import socket

HOST = "192.168.35.142"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)

            if not data:
                break

            received_str = data.decode("utf-8")
            length = len(received_str)
            send_str = "Length of your string is: " + str(length)

            print("Received: " + received_str + ", of length: " + str(length))
            conn.sendall(str.encode(send_str))

        print("Closing connection")
