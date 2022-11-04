# Программа построения графиков

import tkinter as tk
#from tkinter.scrolledtext import ScrolledText as st
#from tkinter import messagebox as mb
#from tkinter import filedialog as fd
#import os
#import pandas as pd

# Функция закрытия программы

def do_close():
    window.destroy()

# Создание главного окна

window = tk.Tk()
window.geometry("450x450")
window.title("Примеры построения графиков")

# Добавление кнопки закрытия программы

btnClose = tk.Button(window, text='Закрыть', font = ('Helvetica', 10, 'bold'), command=do_close)
btnClose.place(x=330, y=400, width=90, height=30)

# Запуск цикла mainloop

window.mainloop()
