import tkinter as tk
from tkinter import ttk
import matplotlib
import pandas as pd

matplotlib.use('TKAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class UserInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Sensor Data')
        self.charts = ['bar', 'line']

        frame= ttk.Frame(self)
        frame.pack(side=tk.TOP, expand=1, anchor='w')


        for x in range(3):
            figure = Figure(figsize=(6, 4), dpi=100)

            figure_canvas = FigureCanvasTkAgg(figure, self)

            figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
            self.axes = figure.add_subplot()


            # add data here

            # function to add data to graphs
            # self.df= pd.DataFrame(data, columns=['language', 'popularity'])



    def callback(self):
        self.axes.clear()
        kind = self.charts[self.cbx.current()]
        self.df.plot(y='y-axis', x='time', kind=kind, ax=self.axes)
        self.axes.set_title('Sensor Data')
        self.axes.set_ylabel('Y-Axis')
        self.axes.figure.canvas.draw()
if __name__ == '__main__':
    ui = UserInterface()
    ui.mainloop()