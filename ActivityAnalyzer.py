import SensorData as SD
import UserInterface as UI

sd = SD.sensorData('DummyData.csv', 'MetaData.csv')
sd.compileSensor()
sd.compileMeta()
gd = sd.compileGraphData()

ui = UI.UserInterface(sd, gd)
ui.root.mainloop()
