import tkinter as tk
from tkinter import messagebox

from rsa_encryption.modular_operations import is_prime, generate_keys, encrypt


class Application:
    def __init__(self):
        window = tk.Tk()
        window.title("RSA Encryption")

        tk.Label(window, text="Message").grid(row=0, column=0)
        self.entry_message = tk.Entry(window)
        self.entry_message.grid(row=0, column=1)

        tk.Label(window, text="p").grid(row=1, column=0)
        self.entry_p = tk.Entry(window)
        self.entry_p.grid(row=1, column=1)

        tk.Label(window, text="q").grid(row=2, column=0)
        self.entry_q = tk.Entry(window)
        self.entry_q.grid(row=2, column=1)

        (tk.Button(window, text="Encrypt", command=self.main)
         .grid(row=3, column=0, columnspan=2))

        self.output = tk.Entry(window)
        self.output.grid(row=4, column=0, columnspan=2)

        window.mainloop()

    @staticmethod
    def alert():
        show_method = getattr(messagebox, "showwarning")
        show_method("Error", "p and q must be prime")

    def main(self):
        p, q = int(self.entry_p.get()), int(self.entry_q.get())
        if not is_prime(p) or not is_prime(q):
            self.alert()
        else:
            n, e = generate_keys(p, q)
            self.output.insert(0, encrypt(self.entry_message.get(), n, e))


Application()
