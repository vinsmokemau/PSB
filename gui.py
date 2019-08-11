"""Gui for show Sin and Cos."""
import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import numpy as np


root = tk.Tk()

canvas1 = tk.Canvas(root, width=1000, height=350)
canvas1.pack()

button1 = tk.Button(root, text='Exit Application', command=root.destroy)
canvas1.create_window(85, 300, window=button1)

entry1 = tk.Entry(root)
canvas1.create_window(100, 200, window=entry1)

entry2 = tk.Entry(root)
canvas1.create_window(100, 220, window=entry2)


def insert_number():
    """."""
    global sin_amp
    global cos_amp

    sin_amp = float(entry1.get())
    cos_amp = float(entry2.get())

    time = np.arange(0, 2 * np.pi, 0.1)

    figure1 = Figure(figsize=(5, 5), dpi=100)

    sin = sin_amp * np.sin(time)
    subplot1 = figure1.add_subplot(121)
    subplot1.plot(time, sin)

    cos = cos_amp * np.cos(time)
    subplot2 = figure1.add_subplot(122)
    subplot2.plot(time, cos)

    plot = FigureCanvasTkAgg(figure1, root)
    plot.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=0)

    figure2 = Figure(figsize=(5, 5), dpi=100)

    add = sin + cos
    subplot3 = figure2.add_subplot(121)
    subplot3.plot(time, add)

    multiplication = sin * cos
    subplot4 = figure2.add_subplot(122)
    subplot4.plot(time, multiplication)

    plot2 = FigureCanvasTkAgg(figure2, root)
    plot2.get_tk_widget().pack()


button2 = tk.Button(root, text='Click to Draw Chart ', command=insert_number)
canvas1.create_window(97, 270, window=button2)

root.mainloop()
