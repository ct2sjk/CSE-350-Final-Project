import tkinter as tk
from tkinter import *
import SensorData as SD
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas
import tkcalendar
from tkcalendar import Calendar, DateEntry

'DummyData'
import matplotlib

matplotlib.use('TKAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

class UserInterface(tk.Tk):

    def __init__(self,sd,gd):
        self.inputtxt = tk
        self.root = Tk()
        self.root.geometry('1920x1080')
        self.root.title('Sensor Data')
        self.sd = sd
        self.gd = gd
        self.gdTemp = gd

        window_frame = Frame(self.root)
        window_frame.pack(expand=True,fill=BOTH)


        tempFrame = Frame(window_frame, width=100, height=200)

        label1 = Label(tempFrame, text="Temperature")
        label1.pack()

        tempFrame.grid(row=0, column=0, padx=10, pady=5)

        figure1 = plt.figure(figsize=(3, 2), dpi=100)

        tempFigure_canvas = FigureCanvasTkAgg(figure1, tempFrame)

        toolbar = NavigationToolbar2Tk(tempFigure_canvas, tempFrame)
        toolbar.update()
        tempFigure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        temp_summarize = Button(tempFrame, text='Summarize', command= self.temp_summarize())
        temp_summarize.pack(side=RIGHT)        
        self.axTemp = figure1.add_subplot()
        gd.dfTemp.plot(x='DateTime', y='Temp', ax=self.axTemp)

        acc_magFrame = Frame(window_frame, width=100, height=200)

        label1 = Label(acc_magFrame, text="Acc Magnitude Average")
        label1.pack()

        acc_magFrame.grid(row=1, column=0, padx=10, pady=5)

        figure2 = plt.figure(figsize=(3, 2), dpi=100)

        acc_magFrame_canvas = FigureCanvasTkAgg(figure2, acc_magFrame)
        toolbar = NavigationToolbar2Tk(acc_magFrame_canvas, acc_magFrame)
        toolbar.update()
        acc_magFrame_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        acc_summarize = Button(acc_magFrame, text='Summarize', command=self.acc_mag_summarize())
        acc_summarize.pack(side=RIGHT)
        self.axACC = figure2.add_subplot()
        gd.dfAcc.plot(x='DateTime', y='ACC Magnitude', ax=self.axACC)

        on_wrist_Frame = Frame(window_frame, width=100, height=200)

        label1 = Label(on_wrist_Frame, text="On Wrist")
        label1.pack()

        on_wrist_Frame.grid(row=2, column=0, padx=10, pady=5)

        figure3 = plt.figure(figsize=(3, 2), dpi=100)

        on_wrist_Frame_canvas = FigureCanvasTkAgg(figure3, on_wrist_Frame)
        toolbar = NavigationToolbar2Tk(on_wrist_Frame_canvas, on_wrist_Frame)
        toolbar.update()
        on_wrist_Frame_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        on_wrist_summarize = Button(on_wrist_Frame, text='Summarize', command=self.on_wrist_summarize())
        on_wrist_summarize.pack(side=RIGHT)
        self.axOnWrist = figure3.add_subplot()
        gd.dfOnWrist.plot(x='DateTime', y='On Wrist', ax=self.axOnWrist)

        step_count_Frame = Frame(window_frame, width=100, height=200)

        label1 = Label(step_count_Frame, text="Step Count")
        label1.pack()

        step_count_Frame.grid(row=0, column=2, padx=10, pady=5)

        figure4 = plt.figure(figsize=(3, 2), dpi=100)

        step_count_Frame_canvas = FigureCanvasTkAgg(figure4, step_count_Frame)
        toolbar = NavigationToolbar2Tk(step_count_Frame_canvas, step_count_Frame)
        toolbar.update()
        step_count_Frame_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        step_count_summarize = Button(step_count_Frame, text='Summarize', command=self.step_count_summarize())
        step_count_summarize.pack(side=RIGHT)
        self.axStepCt = figure4.add_subplot()
        gd.dfStepCt.plot(x='DateTime', y='Step Count', ax=self.axStepCt)

        rest_Frame = Frame(window_frame, width=100, height=200)

        label1 = Label(rest_Frame, text="Rest")
        label1.pack()

        rest_Frame.grid(row=0, column=1, padx=10, pady=5)

        figure5 = plt.figure(figsize=(3, 2), dpi=100)

        rest_Frame_canvas = FigureCanvasTkAgg(figure5, rest_Frame)
        toolbar = NavigationToolbar2Tk(rest_Frame_canvas, rest_Frame)
        toolbar.update()
        rest_Frame_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        rest_summarize = Button(rest_Frame, text='Summarize', command=self.rest_summarize())
        rest_summarize.pack(side=RIGHT)
        self.axRest = figure5.add_subplot()
        gd.dfRest.plot(x='DateTime', y='Rest', ax=self.axRest)

        EDA_Frame = Frame(window_frame, width=100, height=200)

        label1 = Label(EDA_Frame, text="EDA Average")
        label1.pack()

        EDA_Frame.grid(row=1, column=1, padx=10, pady=5)

        figure6 = plt.figure(figsize=(3, 2), dpi=100)

        EDA_Frame_canvas = FigureCanvasTkAgg(figure6, EDA_Frame)
        toolbar = NavigationToolbar2Tk(EDA_Frame_canvas, EDA_Frame)
        toolbar.update()
        EDA_Frame_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        EDA_summarize = Button(EDA_Frame, text='Summarize', command=self.EDA_summarize())
        EDA_summarize.pack(side=RIGHT)
        self.axEDA = figure6.add_subplot()
        gd.dfEDA.plot(x='DateTime', y='EDA', ax=self.axEDA)

        Movement_Frame = Frame(window_frame, width=100, height=200)
        label1 = Label(Movement_Frame, text="Movement Intensity")
        label1.pack()
        Movement_Frame.grid(row=2, column=1, padx=10, pady=5)

        figure7 = plt.figure(figsize=(3, 2), dpi=100)

        Movement_Frame_canvas = FigureCanvasTkAgg(figure7, Movement_Frame)
        toolbar = NavigationToolbar2Tk(Movement_Frame_canvas, Movement_Frame)
        toolbar.update()
        Movement_Frame_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        Movement_summarize = Button(Movement_Frame, text='Summarize', command=self.Movement_summarize())
        Movement_summarize.pack(side=RIGHT)
        self.axMovInten = figure7.add_subplot()
        gd.dfMovInten.plot(x='DateTime', y='Movement Intensity', ax=self.axMovInten)

        QueryFrame = Frame(window_frame, width=100, height=200)

        label1 = Label(QueryFrame, text="Query:")
        label1.pack()


        inputtxt = tk.Text(QueryFrame,
                           height=2,
                           width=20)
        inputtxt.pack()
        inputtxt = tk.Text(QueryFrame,
                           height=2,
                           width=20)
        inputtxt.pack()
        inputtxt = tk.Text(QueryFrame,
                           height=2,
                           width=20)
        inputtxt.pack()
        inputtxt = tk.Text(QueryFrame,
                           height=2,
                           width=20)
        inputtxt.pack()

        aggregate = Button(QueryFrame, text='Aggregate')
        aggregate.pack(side=TOP)
        QueryFrame.grid(row=1, column=2, padx=10, pady=5)

        Compile_Frame = Frame(window_frame, width=100, height=200, padx=10, pady=5)
        Compile_Frame.grid(row=1, column=4, padx=10, pady=5)
        label1 = Label(QueryFrame, text="Menu:", padx=20, pady=100)
        label1.pack()

        plt.show()

    def addNewData(self, summaryFile, metaDataFile):
    #add window for compiling new data with two fields
    #fields open a browse window for file explorer to specify files
    #compile button calls method
        self.sd = SD.sensorData(summaryFile,metaDataFile)
        self.sd.compileSensor()
        self.sd.compileMeta()
        self.gd = self.sd.compileGraphData()
        self.callback()

    def aggregateData(self, DateS, DateE, TimeS, TimeE):
        #returnData = [tempAvrg, ACCMagAvrg, EDAAvrg, onWristAvrg, movIntenAvrg, stepCtAvrg, restAvrg]
        #add window to aggregate based on timeframe
        #window needs start date, end date, start time, and end time
        #add start button on window
        returnData = self.sd.aggregate(DateS, DateE, TimeS, TimeE)
        #somehow plot the return data over graphs
        #self.callback()

    def queryData(self, DateS, DateE, TimeS, TimeE):
        #add window to query based on timeframe
        #window needs start date, end date, start time, and end time
        #add start button on window
        self.gd = self.sd.queryGraph(DateS, DateE, TimeS, TimeE)
        #self.callback()

    def switchGraphData(self):
        #switches between query graphs and full graphs
        gdq = self.gd
        self.gd = self.gdTemp
        self.gdTemp = gdq
        #self.callback()

    def temp_summarize(self):
        #returnData = [sum, highest, lowest]
        returnData = self.sd.summarize('Temp')
        #somehow plot the return data over graphs
        #self.callback()
    def acc_mag_summarize(self):
        #returnData = [sum, highest, lowest]
        returnData = self.sd.summarize('ACCMagnitude')
        #somehow plot the return data over graphs
        #self.callback()
    def on_wrist_summarize(self):
        #returnData = [sum, highest, lowest]
        returnData = self.sd.summarize('OnWrist')
        #somehow plot the return data over graphs
        #self.callback()
    def step_count_summarize(self):
        #returnData = [sum, highest, lowest]
        returnData = self.sd.summarize('StepCount')
        #somehow plot the return data over graphs
        #self.callback()
    def rest_summarize(self):
        #returnData = [sum, highest, lowest]
        returnData = self.sd.summarize('Rest')
        #somehow plot the return data over graphs
        #self.callback()
    def EDA_summarize(self):
        #returnData = [sum, highest, lowest]
        returnData = self.sd.summarize('EDA')
        #somehow plot the return data over graphs
        #self.callback()
    def Movement_summarize(self):
        #returnData = [sum, highest, lowest]
        returnData = self.sd.summarize('MovInten')
        #somehow plot the return data over graphs
        #self.callback()
    def callback(self):
        self.axes.clear()
        self.df.plot(y='y-axis', x='time', ax=self.axes)
        self.axes.set_title('Sensor Data')
        self.axes.set_ylabel('Y-Axis')
        self.axes.figure.canvas.draw()

