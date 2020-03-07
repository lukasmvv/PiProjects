import matplotlib.pyplot as plt
from time import sleep
import csv
from datetime import datetime

data = {'timestamp': [], 'temperature':[], 'humidity': []}

path = r'/home/pi/PiProjects/TempHum/tempHumData.csv'
with open(path,'r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    line = 0

    for row in csv_reader:
        if line == 0:
            print(row)
        else:
            data['timestamp'].append(datetime.strptime(row[0],'%d-%m-%Y %H:%M:%S'))
            data['temperature'].append(float(row[1]))
            data['humidity'].append(float(row[2]))
        line += 1
print(data)

minLen = len(data['timestamp']) - 50
maxLen = -1

print(len(data['timestamp']))
print(len(data['temperature']))
print(len(data['humidity']))
plt.plot(data['timestamp'][minLen:maxLen], data['temperature'][minLen:maxLen], data['timestamp'][minLen:maxLen], data['humidity'][minLen:maxLen])
#plt.plot([1,2,3],[1, 1, 1])
plt.show()
