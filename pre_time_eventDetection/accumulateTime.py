#===================================================================================
#This scrip file to read json file for Earthquake project: Accumulate from SCV(after run CNN)
#Editor: Nguyen Van Quan
#Date edit: 2016 Nov 06
#====================================================================================

#=================
# Libraries
#=================
import re, os
import string 
import sys
import twokenize
import csv
from collections import defaultdict
from os.path import basename
import ntpath
import codecs
import unicodedata
import time

#=============
# Paths
#=============
prccd_folder = "../data" #no backslashes in front of special characters like spaces
prccd_folder = os.path.expanduser(prccd_folder)

#=================
# Functions
#=================
csvfile='FromJsontoRawstream_earthquake16_Pre_CNN.csv'
name = os.path.splitext(csvfile)[0]
print ("Read Json of Tweets -----> CSV file ------> Preprocessing-->CNN------>Accumulation")
def Accumulate(csvfile):
	t0=0;
	inter_count=0;
	m_count=1;
	interval_='20'
	Acc_Tweets=0;
	type_classify='ONE'
	out_time1 = open('%s_Accumulate%ssecondsPred%s_ENGLISH_WORLD.csv'%(name,interval_,type_classify), 'w')
	substring_list=['korea','kr']
        # create the csv writer object
        csv_time1 = csv.writer(out_time1)

	columns = defaultdict(list) # each value in each column is appended to a list

	with open(csvfile, 'rU') as f: 
	#with codecs.open(csvfile, "r", "utf-8") as f:
		reader = csv.DictReader(f) # read rows into a dictionary format
		if type_classify=='ZERO':
			rows = [row for row in reader if row['lang'] == 'en' and row['Pred'] == '0' ]#and any(substring in row['text'] for substring in substring_list)]
		elif type_classify=='ONE':
			rows = [row for row in reader if row['lang'] == 'en' and row['Pred'] == '1' ]#and any(substring in row['text'] for substring in substring_list)]
		else :
		#rows = [row for row in reader if row['Pred'] == '1' and 'korea' in row['text']]
			rows = [row for row in reader if row['lang'] == 'en' ]#and any(substring in row['text'] for substring in substring_list) ]
		for row in rows: # read a row as {column1: value1, column2: value2,...}
			for (k,v) in row.items(): # go over each column name and value 
				columns[k.strip()].append(v) # append the value into the appropriate list based on column name k
				if (k=='timestamp_ms'):
					timestamp_ms=long(v)

					if t0==0:
						t0=timestamp_ms
						
						inter_count=0
					if timestamp_ms<=t0+float(interval_)*1000:
						inter_count+=1
					else:
						csv_time1.writerow([t0,time.strftime('%m/%d/%Y %H:%M:%S',  time.gmtime(t0/1000.)), inter_count])
						no_loop=0;

						while (timestamp_ms > t0+float(interval_)*1000*(2+no_loop)):
							csv_time1.writerow([t0+float(interval_)*1000*(2+no_loop-1),time.strftime('%m/%d/%Y %H:%M:%S',  time.gmtime((t0+float(interval_)*1000*(2+no_loop-1))/1000.)), 0])
							no_loop+=1
						#print "good bye"


						#csv_time1.writerow([t0+float(interval_)*1000*(m_count-1),time.strftime('%m/%d/%Y %H:%M:%S',  time.gmtime((t0+float(interval_)*1000*(m_count-1))/1000.)), inter_count])
						#csv_time1.writerow([timestamp_ms, time.strftime('%m/%d/%Y %H:%M:%S',  time.gmtime(timestamp_ms/1000.)), inter_count])
						Acc_Tweets+=1;
						inter_count=1
						#m_count+=1;
						t0=t0+float(interval_)*1000*(2+no_loop-1)
				 	#csv_time1.writerow(values)
			

		
		print "# Tweets Accummulated datapoint:", Acc_Tweets
		print "# %s Tweets CONSIDERED: " %(type_classify), len(rows)
		#print "# Tweets TOTAL:", len(reader)
	
	out_time1.close()

#=================
# Run
#=================
Accumulate(csvfile)

