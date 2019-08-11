import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

root = tk.Tk()

canvas1 = tk.Canvas(root, width=1000, height=350)
canvas1.pack()

button1 = tk.Button(root, text='Exit Application', command=root.destroy)
canvas1.create_window(85, 300, window=button1)

entry1 = tk.Entry(root)
canvas1.create_window(100, 200, window=entry1)

entry2 = tk.Entry(root)
canvas1.create_window(100, 220, window=entry2)

entry3 = tk.Entry(root)
canvas1.create_window(100, 240, window=entry3)


def insert_number():
    global x1
    global x2
    global x3
    x1 = float(entry1.get())
    x2 = float(entry2.get())
    x3 = float(entry3.get())

    figure1 = Figure(figsize=(5, 5), dpi=100)
    subplot1 = figure1.add_subplot(111)
    subplot1.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])
    plot = FigureCanvasTkAgg(figure1, root)
    plot.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=0)

    figure2 = Figure(figsize=(1, 1), dpi=100)
    subplot2 = figure2.add_subplot(111)
    labels2 = 'Label1', 'Label2', 'Label3'
    pie_sizes = [float(x1), float(x2), float(x3)]
    explode2 = (0, 0.1, 0)
    subplot2.pie(
        pie_sizes,
        explode=explode2,
        labels=labels2,
        autopct='%1.1f%%',
        shadow=True,
        startangle=90,
    )
    subplot2.axis('equal')
    pie2 = FigureCanvasTkAgg(figure2, root)
    pie2.get_tk_widget().pack()


button2 = tk.Button(root, text='Click to Draw Chart ', command=insert_number)
canvas1.create_window(97, 270, window=button2)

root.mainloop()
