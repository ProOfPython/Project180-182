from googletrans import Translator as lang
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Translator')
root.geometry('450x450')
root.config(bg = 'snow')

lblWords = tk.Label(root, bg = 'light blue', text = 'Enter Text:')
lblWords.place(relx = 0.5, rely = 0.3, anchor = tk.CENTER)

txtWords = tk.Text(root, width = 32, height = 4)
txtWords.place(relx = 0.5, rely = 0.4, anchor = tk.N)

root.mainloop()