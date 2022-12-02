import tkinter as tk
from tkinter import *
import matplotlib
import pandas as pd

matplotlib.use('TKAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.widgets import Slider

class UserInterface(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Sensor Data')
        self.geometry('1000x800')

        window_frame = Frame(self)
        window_frame.pack(side=TOP, expand=1)

        window_canvas = Canvas(window_frame)
        window_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        window_scrollbar = Scrollbar(window_frame, orient=VERTICAL, command=window_canvas.yview)
        window_scrollbar.pack(side=RIGHT, fill=Y)

        window_canvas.configure(yscrollcommand=window_scrollbar.set)
        window_canvas.bind('<Configure>', lambda e: window_canvas.configure(scrollregion=window_canvas.bbox("all")))

        tempFrame = Frame(window_frame)

        window_canvas.create_window((0,0), window=tempFrame, anchor="nw")
        tempFrame.pack(side=tk.TOP, expand=1, anchor='w')

        figure = Figure(figsize=(6, 4), dpi=100)

        tempFigure_canvas = FigureCanvasTkAgg(figure, window_frame)

        tempFigure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(tempFigure_canvas, tempFrame)
        toolbar.update()
        temp_summarize = Button(tempFrame, text='Summarize', command= self.temp_summarize())
        aggregate = Button(tempFrame, text='Aggregate')
        temp_summarize.pack(side=RIGHT)
        aggregate.pack(side=RIGHT)
        self.axes = figure.add_subplot()

        acc_magFrame = Frame(window_frame)

        window_canvas.create_window((0,0), window=acc_magFrame, anchor="nw")
        acc_magFrame.pack(side=tk.TOP, expand=1, anchor='w')

        acc_magFrame_canvas = FigureCanvasTkAgg(figure, window_frame)
        toolbar = NavigationToolbar2Tk(acc_magFrame_canvas, acc_magFrame)
        toolbar.update()
        acc_magFrame_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        acc_summarize = Button(acc_magFrame, text='Summarize', command=self.acc_mag_summarize())
        acc_summarize.pack(side=RIGHT)
        self.axes = figure.add_subplot()

        on_wrist_Frame = Frame(window_frame)

        window_canvas.create_window((0, 0), window=on_wrist_Frame, anchor="nw")
        on_wrist_Frame.pack(side=tk.TOP, expand=1, anchor='w')

        on_wrist_Frame_canvas = FigureCanvasTkAgg(figure, window_frame)
        toolbar = NavigationToolbar2Tk(on_wrist_Frame_canvas, on_wrist_Frame)
        toolbar.update()
        on_wrist_Frame_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        on_wrist_summarize = Button(on_wrist_Frame, text='Summarize', command=self.on_wrist_summarize())
        on_wrist_summarize.pack(side=RIGHT)
        self.axes = figure.add_subplot()

        step_count_Frame = Frame(window_frame)

        window_canvas.create_window((0, 0), window=step_count_Frame, anchor="nw")
        step_count_Frame.pack(side=tk.TOP, expand=1, anchor='w')

        step_count_Frame_canvas = FigureCanvasTkAgg(figure, window_frame)
        toolbar = NavigationToolbar2Tk(step_count_Frame_canvas, step_count_Frame)
        toolbar.update()
        step_count_Frame_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        step_count_summarize = Button(step_count_Frame, text='Summarize', command=self.step_count_summarize())
        step_count_summarize.pack(side=RIGHT)
        self.axes = figure.add_subplot()

        rest_Frame = Frame(window_frame)

        window_canvas.create_window((0, 0), window=rest_Frame, anchor="nw")
        rest_Frame.pack(side=tk.TOP, expand=1, anchor='w')

        rest_Frame_canvas = FigureCanvasTkAgg(figure, window_frame)
        toolbar = NavigationToolbar2Tk(rest_Frame_canvas, rest_Frame)
        toolbar.update()
        rest_Frame_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        rest_summarize = Button(rest_Frame, text='Summarize', command=self.rest_summarize())
        rest_summarize.pack(side=RIGHT)
        self.axes = figure.add_subplot()

        EDA_Frame = Frame(window_frame)

        window_canvas.create_window((0, 0), window=EDA_Frame, anchor="nw")
        EDA_Frame.pack(side=tk.TOP, expand=1, anchor='w')

        EDA_Frame_canvas = FigureCanvasTkAgg(figure, self)
        toolbar = NavigationToolbar2Tk(EDA_Frame_canvas, EDA_Frame)
        toolbar.update()
        EDA_Frame_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        EDA_summarize = Button(EDA_Frame, text='Summarize', command=self.EDA_summarize())
        EDA_summarize.pack(side=RIGHT)
        self.axes = figure.add_subplot()

        Movement_Frame = Frame(window_frame)

        window_canvas.create_window((0, 0), window=Movement_Frame, anchor="nw")
        Movement_Frame.pack(side=tk.TOP, expand=1, anchor='w')

        Movement_Frame_canvas = FigureCanvasTkAgg(figure, self)
        toolbar = NavigationToolbar2Tk(Movement_Frame_canvas, Movement_Frame)
        toolbar.update()
        Movement_Frame_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        Movement_summarize = Button(Movement_Frame, text='Summarize', command=self.Movement_summarize())
        Movement_summarize.pack(side=RIGHT)
        self.axes = figure.add_subplot()

        # add data here

        # function to add data to graphs
        # self.df= pd.DataFrame(data, columns=[' ', ' '])

        # temp
        # acc_mag
        # on_wrist
        # step_count
        # rest
        # EDA
        # Movement intensity

    def temp_summarize(self):
        pass
    def acc_mag_summarize(self):
        pass
    def on_wrist_summarize(self):
        pass
    def step_count_summarize(self):
        pass
    def rest_summarize(self):
        pass
    def EDA_summarize(self):
        pass
    def Movement_summarize(self):
        pass

    def callback(self):
        self.axes.clear()
        self.df.plot(y='y-axis', x='time', ax=self.axes)
        self.axes.set_title('Sensor Data')
        self.axes.set_ylabel('Y-Axis')
        self.axes.figure.canvas.draw()
if __name__ == '__main__':
    ui = UserInterface()
    ui.mainloop()