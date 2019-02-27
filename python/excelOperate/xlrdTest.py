'''from xlrd import open_workbook
x_data1=[]
y_data1=[]
wb = open_workbook('phase_detector.xlsx')
for s in wb.sheets():
    print 'Sheet:',s.name
    for row in range(s.nrows):
        print 'the row is:',row
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
        print values
        x_data1.append(values[0])
        y_data1.append(values[1])'''
import matplotlib.pyplot as plt
from xlrd import open_workbook
wb=open_workbook('phase_detector.xlsx')
x_data=[]
y_data=[]
for s in wb.sheets():
    print "this is ",s.name
    for row in range(s.nrows):
        #print "this is ",row
        value=[]
        for col in range(s.ncols):
            value.append(s.cell(row,col).value)
        #print value
        x_data.append(value[0])
        y_data.append(value[1])
#print x_data
#print y_data

plt.plot(x_data,y_data)

plt.xlabel("x")
plt.ylabel("y")
plt.annotate("zero",xy=(180,0),xytext=(60,3),arrowprops=dict(facecolor='black',shrink=0.05),)
plt.show()
