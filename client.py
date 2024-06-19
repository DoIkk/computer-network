import socket

def send_expression(expression):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 9999))
    client_socket.send(expression.encode())

    result = client_socket.recv(1024).decode()
    print(f"서버로부터 받은 결과: {result}")
    client_socket.close()

if __name__ == "__main__":
    while True:
        expression = input("수식을 입력하세요: ")
        if expression.lower() == 'exit':
            break
        send_expression(expression)
