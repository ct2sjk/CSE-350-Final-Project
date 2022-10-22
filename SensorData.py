import pandas as pd
from array import *

class metaData:
    def __init__(self, DateTimeUTC, TimezoneM, App, AppVersion, OS, OSVersion, GTCS):
        self.dateTimeUTC = DateTimeUTC
        self.timezoneM = TimezoneM
        self.app = App
        self.appVersion = AppVersion
        self.OS = OS
        self.OSVersion = OSVersion
        self.GTCS = GTCS

class sensorPoint:
    def __init__(self, Date, Time, Temp, ACCMagnitude, OnWrist, StepCount, Rest):
        self.date = Date
        self.time = Time
        self.temp = Temp
        self.ACCMag = ACCMagnitude
        self.onWrist = OnWrist
        self.stepCt = StepCount
        self.rest = Rest

class graphData:
    def __init__(self, SDarr, SDSize):
        self.SDarr = SDarr
        self.SDSize = SDSize
        self.arrWidth = 3
        self.tempArr = [[0 for x in range(self.arrWidth)] for y in range(self.SDSize)]
        self.ACCMagArr = [[0 for x in range(self.arrWidth)] for y in range(self.SDSize)]
        self.onWristArr = [[0 for x in range(self.arrWidth)] for y in range(self.SDSize)]
        self.stepCtArr = [[0 for x in range(self.arrWidth)] for y in range(self.SDSize)]
        self.restArr = [[0 for x in range(self.arrWidth)] for y in range(self.SDSize)]

    def switcher(self, DataSet):
        iter = 0
        match DataSet:
            case 'Temp':
                for obj in self.SDarr:
                   self.tempArr[iter] = [obj.date, obj.time, obj.temp]
                   iter+=1
            case 'ACCMagnitude':
                for obj in self.SDarr:
                   self.ACCMagArr[iter] = [obj.date, obj.time, obj.ACCMag]
                   iter+=1
            case 'OnWrist':
                for obj in self.SDarr:
                   self.onWristArr[iter] = [obj.date, obj.time, obj.onWrist]
                   iter+=1
            case 'StepCount':
                for obj in self.SDarr:
                   self.stepCtArr[iter] = [obj.date, obj.time, obj.stepCt]
                   iter+=1
            case 'Rest':
                for obj in self.SDarr:
                   self.restArr[iter] = [obj.date, obj.time, obj.rest]
                   iter+=1

    def compileGraph(self):
        self.switcher('Temp')
        self.switcher('ACCMagnitude')
        self.switcher('OnWrist')
        self.switcher('StepCount')
        self.switcher('Rest')

class sensorData:
    def __init__(self, summaryFile, metaDataFile):
        self.summaryFile = summaryFile
        self.metaDataFile = metaDataFile
        self.SDarr = []
        self.MDarr = []
        self.SDSize = 0
        self.MDSize = 0

    def switcher(self, DataSet):
        sum = 0
        highest = 0
        lowest = 0
        iter = 0
        match DataSet:
            case 'Temp':
                for obj in self.SDarr:
                   sum += obj.temp
                   if(iter == 0):
                       highest = obj.temp
                       lowest = obj.temp
                   elif(obj.temp < lowest):
                       lowest = obj.temp
                   elif(obj.temp > highest):
                        highest = obj.temp
                   iter+=1
                return sum,highest,lowest

            case 'ACCMagnitude':
                for obj in self.SDarr:
                   sum += obj.ACCMag
                   if(iter == 0):
                       highest = obj.ACCMag
                       lowest = obj.ACCMag
                   elif(obj.ACCMag < lowest):
                       lowest = obj.ACCMag
                   elif(obj.ACCMag > highest):
                        highest = obj.ACCMag
                   iter+=1
                return sum,highest,lowest

            case 'OnWrist':
                for obj in self.SDarr:
                   sum += obj.onWrist
                   if(iter == 0):
                       highest = obj.onWrist
                       lowest = obj.onWrist
                   elif(obj.onWrist < lowest):
                       lowest = obj.onWrist
                   elif(obj.onWrist > highest):
                        highest = obj.onWrist
                   iter+=1
                return sum,highest,lowest

            case 'StepCount':
                for obj in self.SDarr:
                   sum += obj.stepCt
                   if(iter == 0):
                       highest = obj.stepCt
                       lowest = obj.stepCt
                   elif(obj.stepCt < lowest):
                       lowest = obj.stepCt
                   elif(obj.stepCt > highest):
                        highest = obj.stepCt
                   iter+=1
                return sum,highest,lowest

            case 'Rest':
                for obj in self.SDarr:
                   sum += obj.rest
                   if(iter == 0):
                       highest = obj.rest
                       lowest = obj.rest
                   elif(obj.rest < lowest):
                       lowest = obj.rest
                   elif(obj.rest > highest):
                        highest = obj.rest
                   iter+=1
                return sum,highest,lowest

    def recursiveSearch(self, dateS, timeS, index = 0):
        if index >= self.SDSize:
            return False
        if self.SDarr[index].date == dateS and self.SDarr[index].time >= timeS:
            if self.SDarr[index-1].time < timeS or self.SDarr[index-1].date < dateS:
                return index
            else:
                return self.recursiveSearch(dateS,timeS,index-1)
        else:
            return self.recursiveSearch(dateS,timeS,index+1)


    def compileSensor(self):
        df = pd.read_csv(self.summaryFile)
        df = df.reset_index()
        for index, row in df.iterrows():
            sp = sensorPoint(row['Date'],row['Time'], row['Temp'], row['ACCMagnitude'], row['OnWrist'], row['StepCount'], row['Rest'])
            self.SDarr.append(sp)
        self.SDSize = index + 1

    def compileMeta(self):
        df = pd.read_csv(self.metaDataFile)
        df = df.reset_index()
        for index, row in df.iterrows():
            sp = sensorPoint(row['DateTimeUTC'],row['TimezoneM'], row['App'], row['AppVersion'], row['OS'], row['OSVersion'], row['GTCS'])
            self.MDarr.append(sp)
        self.MDSize = index + 1

    def compileGraphData(self):
        gd = graphData(self.SDarr, self.SDSize)
        return gd

    def summarize(self, DataSet):
        sum,rangeU,rangeL = self.switcher(DataSet)
        average = sum / self.SDSize
        if DataSet == 'OnWrist':
            average = round(average)
        return average,rangeU,rangeL
        
    def aggregate(self, DateS, DateE, TimeS, TimeE):
        tempAvrg = 0
        ACCMagAvrg = 0
        onWristAvrg = 0
        stepCtAvrg = 0
        restAvrg = 0
        indexS = self.recursiveSearch(DateS, TimeS)
        index = indexS
        while self.SDarr[index].date < DateE and self.SDarr[index].time < TimeE:
            tempAvrg += self.SDarr[index].temp
            ACCMagAvrg += self.SDarr[index].ACCMag
            onWristAvrg += self.SDarr[index].onWrist
            stepCtAvrg += self.SDarr[index].stepCt
            restAvrg += self.SDarr[index].rest
            index+=1
        size = index - indexS + 1
        tempAvrg = tempAvrg / size
        ACCMagAvrg = ACCMagAvrg / size
        onWristAvrg = round(onWristAvrg / size)
        stepCtAvrg = stepCtAvrg / size
        restAvrg = restAvrg / size

        return tempAvrg, ACCMagAvrg, onWristAvrg, stepCtAvrg, restAvrg
