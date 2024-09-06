
import socket
import tkinter as tk
from PIL import Image, ImageTk
import pickle
import zlib
import pyautogui

class RemoteViewer:
    def __init__(self, root, host, port):
        self.root = root
        self.host = host
        self.port = port
        self.label = tk.Label(root)
        self.label.pack()
        self.connect_to_server()

    def connect_to_server(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        self.receive_screen()

    def receive_screen(self):
        try:
            data = b""
            while True:
                packet = self.client_socket.recv(4096)
                if not packet:
                    break
                data += packet

            data = zlib.decompress(data)
            screenshot = pickle.loads(data)
            screenshot = ImageTk.PhotoImage(screenshot)
            self.label.config(image=screenshot)
            self.label.image = screenshot
        except Exception as e:
            print(f"Erro ao receber dados: {e}")
        finally:
            self.root.after(100, self.receive_screen)

def main():
    root = tk.Tk()
    viewer = RemoteViewer(root, "127.0.0.1", 9999)
    root.mainloop()

if __name__ == "__main__":
    main()
