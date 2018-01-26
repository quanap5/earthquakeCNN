
#===================================================================================
#This scrip file to read json file for Earthquake project: Moving Average after Accumulate: PreprocessingSCVTime
#Editor: Nguyen Van Quan
#Date edit: 2016 Nov 04
#====================================================================================
import re, os
import string 
import sys
import csv
from collections import defaultdict

from pylab import plot, ylim, xlim, show, xlabel, ylabel, grid
from numpy import linspace, loadtxt, ones, convolve
import numpy as numpy


columns = defaultdict(list) # each value in each column is appended to a list
file_in='FromFromstream_earthquake6interval60_pre1EFilter.csvinterval60_pre1timeE1.csv'
with open(file_in) as f: 
	
	
	#with codecs.open(csvfile, "r", "utf-8") as f:
		reader = csv.DictReader(f) # read rows into a dictionary format
		for row in reader: # read a row as {column1: value1, column2: value2,...}
			for (k,v) in row.items(): # go over each column name and value 
				if k=='label':
					columns[k.strip()].append(float(v)) # append the value into the appropriate list 									     # based on column name k

def movingaverage(interval, window_size):
    window= numpy.ones(int(window_size))/float(window_size)
    return numpy.convolve(interval, window, 'same')


y = columns['label']
#y_av = movingaverage(y, 3)
y_av=numpy.diff(y)
print(y_av)
file_out = os.path.splitext(file_in)[0]
with open('%s_moving.csv'%file_out,'w') as out:
        csv.writer(out, quoting=csv.QUOTE_MINIMAL).writerows(zip(y_av))


	
