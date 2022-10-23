import tkinter as tk
from tkinter import *
import matplotlib
import pandas as pd

matplotlib.use('TKAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class UserInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Sensor Data')
        self.geometry('1000x800')


        for x in range(3):
            frame = Frame(self)

            frame.pack(side=tk.TOP, expand=1, anchor='w')

            figure = Figure(figsize=(6, 4), dpi=100)

            figure_canvas = FigureCanvasTkAgg(figure, self)

            figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

            button1 = Button(frame, text='Summarize')
            button1.pack(side = RIGHT)
            button2 = Button(frame, text='Aggregate')
            button2.pack(side = RIGHT)
            self.axes = figure.add_subplot()


            # add data here

            # function to add data to graphs
            # self.df= pd.DataFrame(data, columns=['language', 'popularity'])

    def callback(self):
        self.axes.clear()
        self.df.plot(y='y-axis', x='time', ax=self.axes)
        self.axes.set_title('Sensor Data')
        self.axes.set_ylabel('Y-Axis')
        self.axes.figure.canvas.draw()
if __name__ == '__main__':
    ui = UserInterface()
    ui.mainloop()