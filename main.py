import tkinter as tk

from app import App
from planet import PLANETS_DATA

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root, PLANETS_DATA)
    root.mainloop()
