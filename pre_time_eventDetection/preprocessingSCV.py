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

#=============
# Paths 
#=============
prccd_folder = "../data" #no backslashes in front of special characters like spaces
prccd_folder = os.path.expanduser(prccd_folder)

#=================
# Functions
#=================
csvfile='FromJsontoRawstream_earthquake16.csv'
print ("Read Json of Tweets -----> CSV file ------> Preprocessing")
def process(lst):
	prccd_item_list=[]
	for tweet in lst:
#		print "[original]", tweet
                #print(tweet)
		# 0. Removing special Characters
		punc = '$%^&*()_+-={}[]:"|\'\~`<>/,'
		trans = string.maketrans(punc, ' '*len(punc))
		tweet = tweet.translate(trans)
		# 1. Normalizing utf8 formatting
		tweet = tweet.decode("unicode-escape").encode("utf8").decode("utf8")
                #tweet = tweet.encode("utf-8")
                tweet = tweet.encode("ascii","ignore")
                tweet = tweet.strip(' \t\n\r')

				# 1. Lowercasing
		tweet = tweet.lower()
#		print "[lowercase]", tweet

		# Word-Level
		tweet = re.sub(' +',' ',tweet) # replace multiple spaces with a single space

		# 2. Normalizing digits
		tweet_words = tweet.strip('\r').split(' ')
		for word in [word for word in tweet_words if word.isdigit()]:
			tweet = tweet.replace(word, "D" * len(word))
#		print "[digits]", tweet

		# 3. Normalizing URLs
		tweet_words = tweet.strip('\r').split(' ')
		for word in [word for word in tweet_words if '/' in word or '.' in word and  len(word) > 3]:
			tweet = tweet.replace(word, "httpAddress")
#		print "[URLs]", tweet

		# 4. Normalizing username
		tweet_words = tweet.strip('\r').split(' ')
		for word in [word for word in tweet_words if word[0] == '@' and len(word) > 1]:
			tweet = tweet.replace(word, "usrId")
#		print "[usrename]", tweet

		# 5. Removing special Characters
		punc = '@$%^&*()_+-={}[]:"|\'\~`<>/,'
		trans = string.maketrans(punc, ' '*len(punc))
		tweet = tweet.translate(trans)
#		print "[punc]", tweet

		# 6. Normalizing +2 elongated char
		tweet = re.sub(r"(.)\1\1+",r'\1\1', tweet.decode('utf-8'))
#		print "[elong]", tweet

		# 7. tokenization using tweetNLP
		tweet = ' '.join(twokenize.simpleTokenize(tweet))
#		print "[token]", tweet 

		#8. fix \n char
		tweet = tweet.replace('\n', ' ')

		prccd_item_list.append(tweet.strip())
#		print "[processed]", tweet.replace('\n', ' ')
	return prccd_item_list

#=====================
# Main Function
#=====================
def filter(csvfile):
	columns = defaultdict(list) # each value in each column is appended to a list

	with open(csvfile, 'rU') as f: 
	#with codecs.open(csvfile, "r", "utf-8") as f:
		reader = csv.DictReader(f) # read rows into a dictionary format
		for row in reader: # read a row as {column1: value1, column2: value2,...}
			for (k,v) in row.items(): # go over each column name and value 
				columns[k.strip()].append(v) # append the value into the appropriate list based on column name k

	prccd_item_list=process(columns['text'])
	name = os.path.splitext(csvfile)[0]
	with open("%s_Pre.csv" % name, 'wb') as f:
	#with codecs.open("%s_AIDR_prccd.csv" % name, 'wb', "utf-8") as f:
		writer = csv.writer(f)
		writer.writerow(['id','created_at','timestamp_ms','user','id_str','lang','geo','text'])
		rows = zip(columns['id'],columns['created_at'],columns['timestamp_ms'],columns['user'],columns['id_str'],columns['lang'],columns['geo'], prccd_item_list)
		for row in rows:
			writer.writerow(row)

#===========
# Run
#===========
filter(csvfile)

