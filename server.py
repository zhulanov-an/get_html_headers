import socket

from config import get_host_random_port

my_socket = socket.socket()

address_and_port = get_host_random_port()
my_socket.bind(address_and_port)
print("Started socket on", address_and_port)
my_socket.listen(10)

conn, addr = my_socket.accept()
print("Got connection", conn, addr)

data = conn.recv(1024)
decoded_data = data.decode("utf-8")
print("Got data", decoded_data)

resp_heads = "HTTP/1.1 200 OK\nContent-Length: 100\n Connection: close\n Content-Type: text/html\n\n"
response = resp_heads + "<body><table><tr><th>header</th><th>value</th></tr>"
for item in decoded_data.split("\r\n")[1:-2]:
    header, *value = item.split(":")
    response += f"<tr><td><b>{header}</b></td><td>{':'.join(value)}</td></tr>"
response += "</table></body>"

conn.send(response.encode("utf-8"))

my_socket.close()
