import matplotlib.pyplot as plt
import csv
import pybursts

x = []
y = []
date_ticks = []


csvfile='FromJsontoRawearthquake_Korea_Pre_CNN_Accumulate30secondsPredONEWORLD.csv'
with open(csvfile,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    i=0;
    for row in plots:
	date_ticks.append(str(row[1]))
        x.append(int(i))
        y.append(int(row[2]))
	i=i+1



#print (pybursts.kleinberg(y, s=10, gamma=1))
plt.plot(x,y, label='Loaded from file!')
#print (y)
#plt.xticks(x, date_ticks)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()

