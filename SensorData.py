import pandas as pd
import numpy as np
from datetime import *


class metaData:
    def __init__(self, DateTimeUTC, TimezoneM, FWVer, App, AppVersion, OS, OSVersion, GTCS):
        self.dateTimeUTC = DateTimeUTC
        self.timezoneM = TimezoneM
        self.firmwareVer = FWVer
        self.app = App
        self.appVersion = AppVersion
        self.OS = OS
        self.OSVersion = OSVersion
        self.GTCS = GTCS


class sensorPoint:
    def __init__(self, Date, Time, Timezone, Temp, ACCMagnitude, EDA, OnWrist, MovementIntensity, StepCount, Rest):
        self.date = Date
        self.time = Time
        self.timeZ = Timezone
        self.temp = Temp
        self.ACCMag = ACCMagnitude
        self.EDA = EDA
        self.onWrist = OnWrist
        self.movInten = MovementIntensity
        self.stepCt = StepCount
        self.rest = Rest


class graphData:
    def __init__(self, SDarr, SDSize):
        self.SDarr = SDarr
        self.SDSize = SDSize
        self.dfTemp = pd.DataFrame()
        self.dfAcc = pd.DataFrame()
        self.dfEDA = pd.DataFrame()
        self.dfOnWrist = pd.DataFrame()
        self.dfMovInten = pd.DataFrame()
        self.dfStepCt = pd.DataFrame()
        self.dfRest = pd.DataFrame()

    def switcher(self, DataSet):
        iter = 0
        d = []
        match DataSet:
            case 'Temp':
                for obj in self.SDarr:
                    d.append({'DateTime': self.parseDateTime(obj.date, obj.time),
                              'TimeZ': obj.timeZ,
                              'Temp': obj.temp
                              })
                    iter += 1
                self.dfTemp = pd.DataFrame(d)
            case 'ACCMagnitude':
                for obj in self.SDarr:
                    d.append({'DateTime': self.parseDateTime(obj.date, obj.time),
                              'TimeZ': obj.timeZ,
                              'ACC Magnitude': obj.ACCMag
                              })
                    iter += 1
                self.dfAcc = pd.DataFrame(d)
            case 'EDA':
                for obj in self.SDarr:
                    d.append({'DateTime': self.parseDateTime(obj.date, obj.time),
                              'TimeZ': obj.timeZ,
                              'EDA': obj.EDA
                              })
                    iter += 1
                self.dfEDA = pd.DataFrame(d)
            case 'OnWrist':
                for obj in self.SDarr:
                    d.append({'DateTime': self.parseDateTime(obj.date, obj.time),
                              'TimeZ': obj.timeZ,
                              'On Wrist': obj.onWrist
                              })
                    iter += 1
                self.dfOnWrist = pd.DataFrame(d)
            case 'MovInten':
                for obj in self.SDarr:
                    d.append({'DateTime': self.parseDateTime(obj.date, obj.time),
                              'TimeZ': obj.timeZ,
                              'Movement Intensity': obj.movInten
                              })
                    iter += 1
                self.dfMovInten = pd.DataFrame(d)
            case 'StepCount':
                for obj in self.SDarr:
                    d.append({'DateTime': self.parseDateTime(obj.date, obj.time),
                              'TimeZ': obj.timeZ,
                              'Step Count': obj.stepCt
                              })
                    iter += 1
                self.dfStepCt = pd.DataFrame(d)
            case 'Rest':
                for obj in self.SDarr:
                    d.append({'DateTime': self.parseDateTime(obj.date, obj.time),
                              'TimeZ': obj.timeZ,
                              'Rest': obj.rest
                              })
                    iter += 1
                self.dfRest = pd.DataFrame(d)

    def parseDateTime(self, date, time):
        time = time.replace('Z', '')
        y, m, d = [int(x) for x in date.split('-')]
        h, mi, s = [int(x) for x in time.split(':')]
        dati = datetime(y, m, d, h, mi, s)
        return dati

    def switcherShift(self, DataSet):
        iter = 0
        d = []
        match DataSet:
            case 'Temp':
                for obj in self.SDarr:
                    dati = self.parseDateTime(obj.date, obj.time)
                    dati += timedelta(minutes=obj.timeZ)
                    d.append({'DateTime': dati,
                              'TimeZ': obj.timeZ,
                              'Temp': obj.temp
                              })
                    iter += 1
                self.dfTemp = pd.DataFrame(d)
            case 'ACCMagnitude':
                for obj in self.SDarr:
                    dati = self.parseDateTime(obj.date, obj.time)
                    dati += timedelta(minutes=obj.timeZ)
                    d.append({'DateTime': dati,
                              'TimeZ': obj.timeZ,
                              'ACC Magnitude': obj.ACCMag
                              })
                    iter += 1
                self.dfAcc = pd.DataFrame(d)
            case 'EDA':
                for obj in self.SDarr:
                    dati = self.parseDateTime(obj.date, obj.time)
                    dati += timedelta(minutes=obj.timeZ)
                    d.append({'DateTime': dati,
                              'TimeZ': obj.timeZ,
                              'EDA': obj.EDA
                              })
                    iter += 1
                self.dfEDA = pd.DataFrame(d)
            case 'OnWrist':
                for obj in self.SDarr:
                    dati = self.parseDateTime(obj.date, obj.time)
                    dati += timedelta(minutes=obj.timeZ)
                    d.append({'DateTime': dati,
                              'TimeZ': obj.timeZ,
                              'On Wrist': obj.onWrist
                              })
                    iter += 1
                self.dfOnWrist = pd.DataFrame(d)
            case 'MovInten':
                for obj in self.SDarr:
                    dati = self.parseDateTime(obj.date, obj.time)
                    dati += timedelta(minutes=obj.timeZ)
                    d.append({'DateTime': dati,
                              'TimeZ': obj.timeZ,
                              'Movement Intensity': obj.movInten
                              })
                    iter += 1
                self.dfMovInten = pd.DataFrame(d)
            case 'StepCount':
                for obj in self.SDarr:
                    dati = self.parseDateTime(obj.date, obj.time)
                    dati += timedelta(minutes=obj.timeZ)
                    d.append({'DateTime': dati,
                              'TimeZ': obj.timeZ,
                              'Step Count': obj.stepCt
                              })
                    iter += 1
                self.dfStepCt = pd.DataFrame(d)
            case 'Rest':
                for obj in self.SDarr:
                    dati = self.parseDateTime(obj.date, obj.time)
                    dati += timedelta(minutes=obj.timeZ)
                    d.append({'DateTime': dati,
                              'TimeZ': obj.timeZ,
                              'Rest': obj.rest
                              })
                    iter += 1
                self.dfRest = pd.DataFrame(d)

    def compileGraphTS(self):
        self.switcherShift('Temp')
        self.switcherShift('ACCMagnitude')
        self.switcherShift('EDA')
        self.switcherShift('OnWrist')
        self.switcherShift('MovInten')
        self.switcherShift('StepCount')
        self.switcherShift('Rest')

    def compileGraph(self):
        self.switcher('Temp')
        self.switcher('ACCMagnitude')
        self.switcher('EDA')
        self.switcher('OnWrist')
        self.switcher('MovInten')
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

            case 'EDA':
                for obj in self.SDarr:
                    sum += obj.EDA
                    if (iter == 0):
                        highest = obj.EDA
                        lowest = obj.EDA
                    elif (obj.EDA < lowest):
                        lowest = obj.EDA
                    elif (obj.EDA > highest):
                        highest = obj.EDA
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

            case 'MovInten':
                for obj in self.SDarr:
                    sum += obj.movInten
                    if (iter == 0):
                        highest = obj.movInten
                        lowest = obj.movInten
                    elif (obj.movInten < lowest):
                        lowest = obj.movInten
                    elif (obj.movInten > highest):
                        highest = obj.movInten
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
        y, m, d = [int(x) for x in dateS.split('-')]
        h, mi, s = [int(x) for x in timeS.split(':')]
        dtS = datetime(y, m, d, h, mi, s)

        if self.parseDateTime(self.SDarr[index].date, self.SDarr[index].time) == dtS or self.parseDateTime(self.SDarr[index].date, self.SDarr[index].time) >= dtS:
            if self.parseDateTime(self.SDarr[index-1].date, self.SDarr[index-1].time) < dtS or self.parseDateTime(self.SDarr[index].date, self.SDarr[index].time) == dtS:
                return index
            else:
                return self.recursiveSearch(dateS, timeS, index-1)
        else:
            return self.recursiveSearch(dateS, timeS, index+1)

    def parseDateTime(self, date, time):
        time = time.replace('Z', '')
        y, m, d = [int(x) for x in date.split('-')]
        h, mi, s = [int(x) for x in time.split(':')]
        dati = datetime(y, m, d, h, mi, s)
        return dati

    def compileSensor(self):
        df = pd.read_csv(self.summaryFile)
        df = df.reset_index()
        ct = 0
        for index, row in df.iterrows():
            datetime = row['Datetime(utc)']
            dateC, timeC = datetime.split('T', 1)
            onWrist = self.bool2int(row['On Wrist'])
            sp = sensorPoint(dateC, timeC, row['Timezone (minutes)'], row['Temp avg'],
                             row['Acc magnitude avg'], row['Eda avg'], onWrist, row['Movement Intensity'], row['Steps count'], row['Rest'])
            self.SDarr.append(sp)
            ct += 1

        self.SDSize = ct + 1

    def compileMeta(self):
        df = pd.read_csv(self.metaDataFile)
        df = df.reset_index()
        ct = 0
        for index, row in df.iterrows():
            sp = metaData(row['DateTime (UTC)'], row['Timezone (minutes)'], row['FW Version'], row['App'],
                             row['App Version'], row['OS'], row['OS Version'], row['GTCS Algorithm Version'])
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

    def aggregate(self, DateS, DateE, TimeS, TimeE, timeShift):
        tempAvrg = 0
        ACCMagAvrg = 0
        EDAAvrg = 0
        onWristAvrg = 0
        movIntenAvrg = 0
        stepCtAvrg = 0
        restAvrg = 0

        returnData = pd.DataFrame()
        df = []

        y, m, d = [int(x) for x in DateE.split('-')]
        h, mi, s = [int(x) for x in TimeE.split(':')]
        dtE = datetime(y, m, d, h, mi, s)

        indexS = self.recursiveSearch(DateS, TimeS)
        index = indexS
        while self.parseDateTime(self.SDarr[index].date, self.SDarr[index].time) < dtE:
            tempAvrg += self.SDarr[index].temp
            ACCMagAvrg += self.SDarr[index].ACCMag
            EDAAvrg += self.SDarr[index].EDA
            onWristAvrg += self.SDarr[index].onWrist
            movIntenAvrg += self.SDarr[index].movInten
            stepCtAvrg += self.SDarr[index].stepCt
            restAvrg += self.SDarr[index].rest
            index += 1
        size = index - indexS
        tempAvrg = tempAvrg / size
        ACCMagAvrg = ACCMagAvrg / size
        EDAAvrg = EDAAvrg / size
        onWristAvrg = round(onWristAvrg / size)
        movIntenAvrg = movIntenAvrg / size
        stepCtAvrg = stepCtAvrg / size
        restAvrg = restAvrg / size

        indexSD = indexS
        if timeShift == True:
            while indexSD <= index:
                dati = self.parseDateTime(self.SDarr[indexSD].date, self.SDarr[indexSD].time)
                dati += timedelta(minutes=self.SDarr[index].timeZ)
                df.append({'DateTime': dati,
                              'TimeZ': self.SDarr[indexSD].timeZ,
                              'TempAvrg': tempAvrg,
                              'ACCAvrg': ACCMagAvrg,
                              'EDAAvrg': EDAAvrg,
                              'OnWristAvrg':onWristAvrg,
                              'MoveIntenAvrg':movIntenAvrg,
                              'StepCtAvrg':stepCtAvrg,
                              'RestAvrg':restAvrg
                              })
                indexSD+=1
        else:
            while indexSD <= index:
                df.append({'DateTime': self.parseDateTime(self.SDarr[indexSD].date, self.SDarr[indexSD].time),
                              'TimeZ': self.SDarr[indexSD].timeZ,
                              'TempAvrg': tempAvrg,
                              'ACCAvrg': ACCMagAvrg,
                              'EDAAvrg': EDAAvrg,
                              'OnWristAvrg':onWristAvrg,
                              'MoveIntenAvrg':movIntenAvrg,
                              'StepCtAvrg':stepCtAvrg,
                              'RestAvrg':restAvrg
                              })
                indexSD+=1
        returnData = pd.DataFrame(df)
        return returnData

    def queryGraph(self, DateS, DateE, TimeS, TimeE):
        y, m, d = [int(x) for x in DateE.split('-')]
        h, mi, s = [int(x) for x in TimeE.split(':')]
        dtE = datetime(y, m, d, h, mi, s)

        SDarrQ = []

        indexS = self.recursiveSearch(DateS, TimeS)
        index = indexS
        while self.parseDateTime(self.SDarr[index].date, self.SDarr[index].time) <= dtE:
            sp = sensorPoint(self.SDarr[index].date, self.SDarr[index].time, self.SDarr[index].timeZ, self.SDarr[index].temp, self.SDarr[index].ACCMag,
                             self.SDarr[index].EDA, self.SDarr[index].onWrist, self.SDarr[index].movInten, self.SDarr[index].stepCt, self.SDarr[index].rest)

            SDarrQ.append(sp)
            index += 1
        SDarrQsize = index - indexS
        gd = graphData(SDarrQ, SDarrQsize)
        gd.compileGraph()
        return gd

