
import socket
import threading
import pyautogui
import pickle
import zlib

def capture_screen():
    screenshot = pyautogui.screenshot()
    screenshot = screenshot.resize((800, 600))
    return screenshot

def handle_client(client_socket):
    while True:
        try:
            screenshot = capture_screen()
            data = pickle.dumps(screenshot)
            data = zlib.compress(data)
            client_socket.sendall(data)
        except Exception as e:
            print(f"Erro ao enviar dados: {e}")
            break

    client_socket.close()

def start_server(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Servidor ouvindo em {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        print(f"Conexão aceita de {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server("0.0.0.0", 9999)
