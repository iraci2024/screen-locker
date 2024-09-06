
import tkinter as tk
import keyboard
import mouse
import threading

class ScreenLocker:
    def __init__(self, root):
        self.root = root
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-topmost", True)
        self.root.config(cursor="none")

        self.password = "1234"  # Defina a senha aqui

        self.create_widgets()
        self.block_input()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Digite a senha para desbloquear", font=("Helvetica", 24), bg="black", fg="white")
        self.label.pack(pady=20)

        self.entry = tk.Entry(self.root, font=("Helvetica", 24), show="*")
        self.entry.pack(pady=20)
        self.entry.bind("<Return>", self.check_password)

        self.button = tk.Button(self.root, text="Desbloquear", font=("Helvetica", 24), command=self.check_password)
        self.button.pack(pady=20)

    def check_password(self, event=None):
        if self.entry.get() == self.password:
            self.root.destroy()
            self.unblock_input()

    def block_input(self):
        self.blocking = True
        threading.Thread(target=self._block_input).start()

    def _block_input(self):
        while self.blocking:
            keyboard.block_key('all')
            mouse.move(0, 0)

    def unblock_input(self):
        self.blocking = False
        keyboard.unhook_all()
        mouse.unhook_all()

def main():
    root = tk.Tk()
    app = ScreenLocker(root)
    root.mainloop()

if __name__ == "__main__":
    main()
