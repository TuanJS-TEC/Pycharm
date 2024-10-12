import socket

def handle_client(client_socket):
  """Xử lý kết nối từ client."""
  while True:
    try:
      data = client_socket.recv(1024).decode('utf-8')
      if not data:
        break
      print(f"Received from client: {data}")
      # Chuyển đổi chuỗi sang chữ hoa
      modified_data = data.upper()
      client_socket.send(modified_data.encode('utf-8'))
    except Exception as e:
      print(f"Error handling client: {e}")
      break
  client_socket.close()

def start_server():
  """Khởi động TCP Server."""
  host = '127.0.0.1'  # Địa chỉ IP của máy chủ (localhost)
  port = 65432        # Cổng bất kỳ

  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Server started on {host}:{port}")

    while True:
      client_socket, addr = server_socket.accept()
      print(f"Accepted connection from {addr}")
      handle_client(client_socket)

if __name__ == "__main__":
  start_server()