from googletrans import Translator as lang
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Translator')
root.geometry('700x400')
root.config(bg = 'MistyRose1')

lblInput = tk.Label(root, bg = 'light blue', text = 'Language:')
lblInput.place(relx = 0.2, rely = 0.3, anchor = tk.E)
entInput = tk.Entry(root)
entInput.place(relx = 0.2, rely = 0.3, anchor = tk.W)
txtInput = tk.Text(root, width = 32, height = 8)
txtInput.place(relx = 0.25, rely = 0.4, anchor = tk.N)

lblOutput = tk.Label(root, bg = 'light blue', text = 'Language:')
lblOutput.place(relx = 0.7, rely = 0.3, anchor = tk.E)
entOutput = tk.Entry(root)
entOutput.place(relx = 0.7, rely = 0.3, anchor = tk.W)
txtOutput = tk.Text(root, width = 32, height = 8)
txtOutput.place(relx = 0.75, rely = 0.4, anchor = tk.N)

btnLang = tk.Button(root, bg = 'salmon1', text = 'Translate')
btnLang.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)

root.mainloop()