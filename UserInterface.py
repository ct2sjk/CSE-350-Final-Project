from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import matplotlib
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import SensorData as SD
from click import command
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import sys

sys.setrecursionlimit(10 ** 5)

matplotlib.use('TKAgg')


class UserInterface(tk.Tk):

    def __init__(self, sd, gd):
        self.root = Tk()
        self.root.geometry('1920x1080')
        self.root.title('Sensor Data')
        self.sd = sd
        self.gd = gd
        self.gdTemp = gd
        self.timeShift = False
        self.summaryFile = ''
        self.metaDataFile = ''

        window_frame = Frame(self.root)
        window_frame.pack(expand=True, fill=BOTH)

        tempFrame = Frame(window_frame, width=100, height=200)
        label1 = Label(tempFrame, text="Temperature")
        label1.pack()
        tempFrame.grid(row=0, column=0, padx=10, pady=5)
        self.figure1 = plt.figure(figsize=(3, 2), dpi=100)
        tempFigure_canvas = FigureCanvasTkAgg(self.figure1, tempFrame)
        toolbar = NavigationToolbar2Tk(tempFigure_canvas, tempFrame)
        toolbar.update()
        tempFigure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        temp_summarize = Button(
            tempFrame, text='Summarize', command=self.temp_summarize)
        temp_summarize.pack(side=RIGHT)

        acc_magFrame = Frame(window_frame, width=100, height=200)
        label1 = Label(acc_magFrame, text="Acc Magnitude Average")
        label1.pack()
        acc_magFrame.grid(row=1, column=0, padx=10, pady=5)
        self.figure2 = plt.figure(figsize=(3, 2), dpi=100)
        acc_magFrame_canvas = FigureCanvasTkAgg(self.figure2, acc_magFrame)
        toolbar = NavigationToolbar2Tk(acc_magFrame_canvas, acc_magFrame)
        toolbar.update()
        acc_magFrame_canvas.get_tk_widget().pack(
            side=tk.TOP, fill=tk.BOTH, expand=True)
        acc_summarize = Button(
            acc_magFrame, text='Summarize', command=self.acc_mag_summarize)
        acc_summarize.pack(side=RIGHT)

        on_wrist_Frame = Frame(window_frame, width=100, height=200)
        label1 = Label(on_wrist_Frame, text="On Wrist")
        label1.pack()
        on_wrist_Frame.grid(row=2, column=0, padx=10, pady=5)
        self.figure3 = plt.figure(figsize=(3, 2), dpi=100)
        on_wrist_Frame_canvas = FigureCanvasTkAgg(self.figure3, on_wrist_Frame)
        toolbar = NavigationToolbar2Tk(on_wrist_Frame_canvas, on_wrist_Frame)
        toolbar.update()
        on_wrist_Frame_canvas.get_tk_widget().pack(
            side=tk.TOP, fill=tk.BOTH, expand=True)
        on_wrist_summarize = Button(
            on_wrist_Frame, text='Summarize', command=self.on_wrist_summarize)
        on_wrist_summarize.pack(side=RIGHT)

        step_count_Frame = Frame(window_frame, width=100, height=200)
        label1 = Label(step_count_Frame, text="Step Count")
        label1.pack()
        step_count_Frame.grid(row=0, column=2, padx=10, pady=5)
        self.figure4 = plt.figure(figsize=(3, 2), dpi=100)
        step_count_Frame_canvas = FigureCanvasTkAgg(self.figure4, step_count_Frame)
        toolbar = NavigationToolbar2Tk(
            step_count_Frame_canvas, step_count_Frame)
        toolbar.update()
        step_count_Frame_canvas.get_tk_widget().pack(
            side=tk.TOP, fill=tk.BOTH, expand=True)
        step_count_summarize = Button(
            step_count_Frame, text='Summarize', command=self.step_count_summarize)
        step_count_summarize.pack(side=RIGHT)

        rest_Frame = Frame(window_frame, width=100, height=200)
        label1 = Label(rest_Frame, text="Rest")
        label1.pack()
        rest_Frame.grid(row=0, column=1, padx=10, pady=5)
        self.figure5 = plt.figure(figsize=(3, 2), dpi=100)
        rest_Frame_canvas = FigureCanvasTkAgg(self.figure5, rest_Frame)
        toolbar = NavigationToolbar2Tk(rest_Frame_canvas, rest_Frame)
        toolbar.update()
        rest_Frame_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        rest_summarize = Button(
            rest_Frame, text='Summarize', command=self.rest_summarize)
        rest_summarize.pack(side=RIGHT)

        EDA_Frame = Frame(window_frame, width=100, height=200)
        label1 = Label(EDA_Frame, text="EDA Average")
        label1.pack()
        EDA_Frame.grid(row=1, column=1, padx=10, pady=5)
        self.figure6 = plt.figure(figsize=(3, 2), dpi=100)
        EDA_Frame_canvas = FigureCanvasTkAgg(self.figure6, EDA_Frame)
        toolbar = NavigationToolbar2Tk(EDA_Frame_canvas, EDA_Frame)
        toolbar.update()
        EDA_Frame_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        EDA_summarize = Button(EDA_Frame, text='Summarize',
                               command=self.EDA_summarize)
        EDA_summarize.pack(side=RIGHT)

        Movement_Frame = Frame(window_frame, width=100, height=200)
        label1 = Label(Movement_Frame, text="Movement Intensity")
        label1.pack()
        Movement_Frame.grid(row=2, column=1, padx=10, pady=5)
        self.figure7 = plt.figure(figsize=(3, 2), dpi=100)
        Movement_Frame_canvas = FigureCanvasTkAgg(self.figure7, Movement_Frame)
        toolbar = NavigationToolbar2Tk(Movement_Frame_canvas, Movement_Frame)
        toolbar.update()
        Movement_Frame_canvas.get_tk_widget().pack(
            side=tk.TOP, fill=tk.BOTH, expand=True)
        Movement_summarize = Button(
            Movement_Frame, text='Summarize', command=self.Movement_summarize)
        Movement_summarize.pack(side=RIGHT)
     

        QueryFrame = Frame(window_frame, width=100, height=200)

        label1 = Label(QueryFrame, text="Query:")
        label1.pack()
        QueryFrame.grid(row=1, column=2, padx=10, pady=5)

        self.inputtxt1 = tk.Text(QueryFrame,
                                 height=2,
                                 width=20)
        self.inputtxt1.pack()
        self.inputtxt2 = tk.Text(QueryFrame,
                                 height=2,
                                 width=20)
        self.inputtxt2.pack()
        self.inputtxt3 = tk.Text(QueryFrame,
                                 height=2,
                                 width=20)
        self.inputtxt3.pack()
        self.inputtxt4 = tk.Text(QueryFrame,
                                 height=2,
                                 width=20)
        self.inputtxt4.pack()

        aggregate = Button(QueryFrame, text='Aggregate',
                           command=self.aggregateData)
        aggregate.pack(side=TOP)

        Compile_Frame = Frame(window_frame, width=100, height=200)
        Compile_Frame.grid(row=2, column=2, padx=10, pady=5)

        label1 = Label(Compile_Frame, text="Menu:", padx=10, pady=5)
        label1.pack()

        Browse = Button(Compile_Frame, text="Browse SensorData", padx=20, pady=10, command=self.browseFileSD)
        Browse.pack(padx=10, pady=5)

        Browse = Button(Compile_Frame, text="Browse MetaData", padx=20, pady=10, command=self.browseFileMD)
        Browse.pack(padx=10, pady=5)

        Compile = Button(Compile_Frame, text="Compile", padx=10, pady=10, command=self.addNewData)
        Compile.pack(side=TOP, padx=10, pady=5)

        Timeshift = Button(Compile_Frame, text="Timeshift", padx=10, pady=10, command=self.switchTimeSeries)
        Timeshift.pack(side=RIGHT, padx=10, pady=5)

        Quit = Button(Compile_Frame, text="  Quit  ",
                      padx=10, pady=10, command=self.quit)
        Quit.pack(side=RIGHT, padx=10, pady=6)

        Query = Button(QueryFrame, text="Query", command=self.queryData)
        Query.pack(side=TOP)

        Swap = Button(QueryFrame, text=" Swap ", command=self.switchGraphData)
        Swap.pack(side=TOP)

        Output_Frame = Frame(window_frame, width=100, height=200)

        label1 = Label(Output_Frame, text="General Output:")
        label1.pack()
        Output_Frame.grid(row=1, column=3, padx=10, pady=5)

        self.outputtxt1 = tk.Text(Output_Frame,
                                  height=20,
                                  width=60)
        self.outputtxt1.pack()
        Delete = Button(Output_Frame, text="Delete", command=lambda: self.outputtxt1.delete(1.0, END))
        Delete.pack()

        self.regraph()
    def addNewData(self):
        # add window for compiling new data with two fields
        # fields open a browse window for file explorer to specify files
        # compile button calls method
        self.sd = SD.sensorData(self.summaryFile, self.metaDataFile)
        self.sd.compileSensor()
        self.sd.compileMeta()
        self.callback()
        self.gd = self.sd.compileGraphData()
        self.regraph()

    def switchTimeSeries(self):
        self.callback()
        if self.timeShift == True:
            self.gdTemp = self.gd
            self.gd.compileGraph()
            self.timeShift = False
        else:
            self.gdTemp = self.gd
            self.gd.compileGraphTS()
            self.timeShift = True
        self.regraph()
        
    def aggregateData(self):
        DateS = self.inputtxt1.get('1.0', 'end-1c')
        DateE = self.inputtxt2.get('1.0', 'end-1c')
        TimeS = self.inputtxt3.get('1.0', 'end-1c')
        TimeE = self.inputtxt4.get('1.0', 'end-1c')
        returnData = self.sd.aggregate(
            DateS, DateE, TimeS, TimeE, self.timeShift)

        self.callback()
        self.regraph()
        returnData.plot(x='DateTime', y='TempAvrg', ax=self.axTemp)
        returnData.plot(x='DateTime', y='ACCAvrg', ax=self.axACC)
        returnData.plot(x='DateTime', y='EDAAvrg', ax=self.axEDA)
        returnData.plot(x='DateTime', y='OnWristAvrg', ax=self.axOnWrist)
        returnData.plot(x='DateTime', y='MoveIntenAvrg', ax=self.axMovInten)
        returnData.plot(x='DateTime', y='StepCtAvrg', ax=self.axStepCt)
        returnData.plot(x='DateTime', y='RestAvrg', ax=self.axRest)
        plt.show()

    def queryData(self):
        # add window to query based on timeframe
        # window needs start date, end date, start time, and end time
        # add start button on window
        DateS = self.inputtxt1.get('1.0', 'end-1c')
        DateE = self.inputtxt2.get('1.0', 'end-1c')
        TimeS = self.inputtxt3.get('1.0', 'end-1c')
        TimeE = self.inputtxt4.get('1.0', 'end-1c')
        self.callback()
        self.gd = self.sd.queryGraph(DateS, DateE, TimeS, TimeE)
        self.regraph()        

    def switchGraphData(self):
        # switches between query graphs and full graphs
        self.callback()
        gdq = self.gd
        self.gd = self.gdTemp
        self.gdTemp = gdq
        self.regraph()

    def temp_summarize(self):
        # returnData = [sum, highest, lowest]
        self.callback()
        returnData = self.sd.summarize('Temp')
        # format return data
        Temp_String = self.stringFormat("Temperature", returnData)
        self.outputtxt1.insert(tk.END, Temp_String)

    def acc_mag_summarize(self):
        # returnData = [sum, highest, lowest]
        self.regraph()
        returnData = self.sd.summarize('ACCMagnitude')
        # format return data
        ACC_Mag_String = self.stringFormat("ACC_Magnitude", returnData)
        self.outputtxt1.insert(tk.END, ACC_Mag_String)

    def on_wrist_summarize(self):
        # returnData = [sum, highest, lowest]
        returnData = self.sd.summarize('OnWrist')
        # format return data
        On_Wrist_String = self.stringFormat("On_Wrist", returnData)
        self.outputtxt1.insert(tk.END, On_Wrist_String)

    def step_count_summarize(self):
        # returnData = [sum, highest, lowest]
        returnData = self.sd.summarize('StepCount')
        # format return data
        Step_Count_String = self.stringFormat("Step_Count", returnData)
        self.outputtxt1.insert(tk.END, Step_Count_String)

    def rest_summarize(self):
        # returnData = [sum, highest, lowest]
        returnData = self.sd.summarize('Rest')
        # format return data
        Rest_String = self.stringFormat("Rest", returnData)
        self.outputtxt1.insert(tk.END, Rest_String)

    def EDA_summarize(self):
        # returnData = [sum, highest, lowest]
        returnData = self.sd.summarize('EDA')
        # format return data
        EDA_String = self.stringFormat("EDA", returnData)
        self.outputtxt1.insert(tk.END, EDA_String)

    def Movement_summarize(self):
        # returnData = [sum, highest, lowest]
        returnData = self.sd.summarize('MovInten')
        # format return data
        Movement_String = self.stringFormat("Movement", returnData)
        self.outputtxt1.insert(tk.END, Movement_String)

    def stringFormat(self, title, numList):
        strFormat = "Summary " + "(" + title + "):" + "\n" + "Sum: " + str(numList[0]) + "\n" + "Min: " + str(
            numList[2]) + "\n" + "Max: " + str(numList[1]) + "\n"

        return strFormat

    def callback(self):
        self.figure1.clf()
        self.figure2.clf()
        self.figure3.clf()
        self.figure4.clf()
        self.figure5.clf()
        self.figure6.clf()
        self.figure7.clf()
        plt.show()

    def regraph(self):
        self.axTemp = self.figure1.add_subplot()
        self.axACC = self.figure2.add_subplot()
        self.axOnWrist = self.figure3.add_subplot()
        self.axStepCt = self.figure4.add_subplot()
        self.axRest = self.figure5.add_subplot()
        self.axEDA = self.figure6.add_subplot()
        self.axMovInten = self.figure7.add_subplot()

        self.gd.dfTemp.plot(x='DateTime', y='Temp', ax=self.axTemp)
        self.gd.dfAcc.plot(x='DateTime', y='ACC Magnitude', ax=self.axACC)
        self.gd.dfEDA.plot(x='DateTime', y='EDA', ax=self.axEDA)
        self.gd.dfOnWrist.plot(x='DateTime', y='On Wrist', ax=self.axOnWrist)
        self.gd.dfMovInten.plot(x='DateTime', y='Movement Intensity', ax=self.axMovInten)
        self.gd.dfStepCt.plot(x='DateTime', y='Step Count', ax=self.axStepCt)
        self.gd.dfRest.plot(x='DateTime', y='Rest', ax=self.axRest)
        plt.show()    

    def browseFileSD(self):
        # Add this to main project
        filename = filedialog.askopenfilename(
            initialdir="/", title='Choose a file', filetypes=[('CSV Files', '.*csv')])
        self.summaryFile = filename

    def browseFileMD(self):
        # Add this to main project
        filename = filedialog.askopenfilename(
            initialdir="/", title='Choose a file', filetypes=[('CSV Files', '.*csv')])
        self.metaDataFile = filename