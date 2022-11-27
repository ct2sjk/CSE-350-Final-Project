import pandas as pd
import numpy as np
from datetime import *
"""
To do: 
Add time offset for timezone (compile sensor)
Add timezone to dataframe (graphdata)
"""



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
        self.dfTemp = pd.DataFrame()
        self.dfAcc = pd.DataFrame()
        self.dfOnWrist = pd.DataFrame()
        self.dfStepCt = pd.DataFrame()
        self.dfRest = pd.DataFrame()

    def switcher(self, DataSet):
        iter = 0
        d = []
        match DataSet:
            case 'Temp':
                for obj in self.SDarr:
                    d.append({'DateTime': self.parseDateTime(obj.date, obj.time), 
                              'Temp': obj.temp

                              })
                    iter += 1
                self.dfTemp = pd.DataFrame(d)
            case 'ACCMagnitude':
                for obj in self.SDarr:
                    d.append({'DateTime': self.parseDateTime(obj.date, obj.time), 
                              'Temp': obj.ACCMag

                              })
                    iter += 1
                self.dfAcc = pd.DataFrame(d)
            case 'OnWrist':
                for obj in self.SDarr:
                    d.append({'DateTime': self.parseDateTime(obj.date, obj.time), 
                              'Temp': obj.onWrist

                              })
                    iter += 1
                self.dfOnWirst = pd.DataFrame(d)
            case 'StepCount':
                for obj in self.SDarr:
                    d.append({'DateTime': self.parseDateTime(obj.date, obj.time), 
                              'Temp': obj.stepCt

                              })
                    iter += 1
                self.dfStepCt = pd.DataFrame(d)
            case 'Rest':
                for obj in self.SDarr:
                    d.append({'DateTime': self.parseDateTime(obj.date, obj.time), 
                              'Temp': obj.rest

                              })
                    iter += 1
                self.dfRest = pd.DataFrame(d)

    def parseDateTime(self,date,time):
        time = time.replace('Z','')
        y,m,d = [int(x) for x in date.split('-')]
        h,mi,s = [int(x) for x in time.split(':')]
        dati = datetime(y,m,d,h,mi,s)
        return dati    

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

    def switcherSum(self, DataSet):
        sum = 0.0
        highest = 0.0
        lowest = 0.0
        iter = 0
        returnData = [sum, highest, lowest]
        match DataSet:
            case 'Temp':
                for obj in self.SDarr:
                    sum += obj.temp
                    if (iter == 0):
                        highest = obj.temp
                        lowest = obj.temp
                    elif (obj.temp < lowest):
                        lowest = obj.temp
                    elif (obj.temp > highest):
                        highest = obj.temp
                    iter += 1
                    returnData = [sum, highest, lowest]

            case 'ACCMagnitude':
                for obj in self.SDarr:
                    sum += obj.ACCMag
                    if (iter == 0):
                        highest = obj.ACCMag
                        lowest = obj.ACCMag
                    elif (obj.ACCMag < lowest):
                        lowest = obj.ACCMag
                    elif (obj.ACCMag > highest):
                        highest = obj.ACCMag
                    iter += 1
                    returnData = [sum, highest, lowest]

            case 'OnWrist':
                for obj in self.SDarr:
                    sum += obj.onWrist
                    if (iter == 0):
                        highest = obj.onWrist
                        lowest = obj.onWrist
                    elif (obj.onWrist < lowest):
                        lowest = obj.onWrist
                    elif (obj.onWrist > highest):
                        highest = obj.onWrist
                    iter += 1
                    returnData = [sum, highest, lowest]

            case 'StepCount':
                for obj in self.SDarr:
                    sum += obj.stepCt
                    if (iter == 0):
                        highest = obj.stepCt
                        lowest = obj.stepCt
                    elif (obj.stepCt < lowest):
                        lowest = obj.stepCt
                    elif (obj.stepCt > highest):
                        highest = obj.stepCt
                    iter += 1
                    returnData = [sum, highest, lowest]

            case 'Rest':
                for obj in self.SDarr:
                    sum += obj.rest
                    if (iter == 0):
                        highest = obj.rest
                        lowest = obj.rest
                    elif (obj.rest < lowest):
                        lowest = obj.rest
                    elif (obj.rest > highest):
                        highest = obj.rest
                    iter += 1
                    returnData = [sum, highest, lowest]
        return returnData

    def bool2int(self, val):
        match val:
            case True:
                return 1
            case False:
                return 0

    def recursiveSearch(self, dateS, timeS, index=0):
        if index >= self.SDSize:
            return False
        y,m,d = [int(x) for x in dateS.split('-')]
        h,mi,s = [int(x) for x in timeS.split(':')]
        dtS = datetime(y,m,d,h,mi,s)

        if self.parseDateTime(self.SDarr[index].date,self.SDarr[index].time) == dtS and self.parseDateTime(self.SDarr[index].date,self.SDarr[index].time) >= dtS:
            if self.parseDateTime(self.SDarr[index-1].date,self.SDarr[index-1].time) < dtS or self.parseDateTime(self.SDarr[index].date,self.SDarr[index].time) == dtS:
                return index
            else:
                return self.recursiveSearch(dateS, timeS, index-1)
        else:
            return self.recursiveSearch(dateS, timeS, index+1)
    def parseDateTime(self,date,time):
        time = time.replace('Z','')
        y,m,d = [int(x) for x in date.split('-')]
        h,mi,s = [int(x) for x in time.split(':')]
        dati = datetime(y,m,d,h,mi,s)
        return dati       

    def compileSensor(self):
        df = pd.read_csv(self.summaryFile)
        df = df.reset_index()
        ct = 0
        for index, row in df.iterrows():
            date, time = row['Datetime(utc)'].split('T', 1)
            onWrist = self.bool2int(row['On Wrist'])
            sp = sensorPoint(date, time, row['Temp avg'],
                             row['Acc magnitude avg'], onWrist, row['Steps count'], row['Rest'])
            self.SDarr.append(sp)
            ct += 1

        self.SDSize = ct + 1

    def compileMeta(self):
        df = pd.read_csv(self.metaDataFile)
        df = df.reset_index()
        ct = 0
        for index, row in df.iterrows():
            sp = sensorPoint(row['DateTimeUTC'], row['TimezoneM'], row['App'],
                             row['AppVersion'], row['OS'], row['OSVersion'], row['GTCS'])
            self.MDarr.append(sp)
            ct += 1
        self.MDSize = ct + 1

    def compileGraphData(self):
        gd = graphData(self.SDarr, self.SDSize)
        gd.compileGraph()
        return gd

    def summarize(self, DataSet):
        returnedData = [0.0, 0.0, 0.0]
        returnedData = self.switcherSum(DataSet)
        rSum = returnedData[0]
        rangeU = returnedData[1]
        rangeL = returnedData[2]
        average = rSum / self.SDSize
        if DataSet == 'OnWrist':
            average = round(average)
        return average, rangeU, rangeL

    def aggregate(self, DateS, DateE, TimeS, TimeE):
        tempAvrg = 0
        ACCMagAvrg = 0
        onWristAvrg = 0
        stepCtAvrg = 0
        restAvrg = 0

        y,m,d = [int(x) for x in DateE.split('-')]
        h,mi,s = [int(x) for x in TimeE.split(':')]
        dtE = datetime(y,m,d,h,mi,s)

        indexS = self.recursiveSearch(DateS, TimeS)
        index = indexS
        while self.parseDateTime(self.SDarr[index].date,self.SDarr[index].time) <= dtE:
            tempAvrg += self.SDarr[index].temp
            ACCMagAvrg += self.SDarr[index].ACCMag
            onWristAvrg += self.SDarr[index].onWrist
            stepCtAvrg += self.SDarr[index].stepCt
            restAvrg += self.SDarr[index].rest
            index += 1
        size = index - indexS
        tempAvrg = tempAvrg / size
        ACCMagAvrg = ACCMagAvrg / size
        onWristAvrg = round(onWristAvrg / size)
        stepCtAvrg = stepCtAvrg / size
        restAvrg = restAvrg / size

        return tempAvrg, ACCMagAvrg, onWristAvrg, stepCtAvrg, restAvrg


if __name__ == '__main__':
    sd = sensorData('DummyData.csv', 'DummyData.csv')
    sd.compileSensor()
    print(sd.summarize('OnWrist'))
    print(sd.aggregate('2019-09-20','2019-09-20','11:49:00', '11:52:00'))
    gd = sd.compileGraphData()
    print(gd.dfTemp)
