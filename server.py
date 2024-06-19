import socket

def evaluate_expression(expression):
    try:
        # Evaluate the expression and return the result
        result = eval(expression)
        return str(result)
    except Exception as e:
        return "에러: 수식이 잘못되었습니다."

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9999))
    server_socket.listen(1)
    print("서버가 시작되었습니다. 클라이언트를 기다리는 중...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"클라이언트가 연결되었습니다: {addr}")
        data = client_socket.recv(1024).decode()
        print(f"받은 데이터: {data}")
        
        result = evaluate_expression(data)
        client_socket.send(result.encode())
        client_socket.close()

if __name__ == "__main__":
    start_server()
