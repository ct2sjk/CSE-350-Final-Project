"""
Add default sd to be passed to UI object (pass by reference)
Create as executable
"""
import SensorData as SD
import UserInterface as UI

if __name__ == '__main__':
    sd = SD.sensorData('DummyData.csv', 'MetaData.csv')
    sd.compileSensor()
    sd.compileMeta()
    gd = sd.compileGraphData()

    ui = UI.UserInterface(sd,gd)
    ct = 0
    if ct < 1:
        ui.root.mainloop()
        ct+=1
