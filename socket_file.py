import socket

form_protocol = input("What form do you to send yout packet: ")

if form_protocol=='TCP':

    target_host = "www.google.com"
    target_port = 80

    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connet the client
    client.connect((target_host, target_port))

    # send some data
    client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

    # receive some data
    response = client.recv(4096)
    print(response.decode())
    client.close

if form_protocol=='UDP':

    target_host = "127.0.0.1"
    target_port = 9997
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.sendto(b"AAABBBCCC", (target_host, target_port))
    data, addr = client.recvfrom(4096)
    print(data.decode())
    client.close
