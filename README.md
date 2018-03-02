# earthquake detection using social media

0. Requirementes:
	Ubuntu
	python 2.7>
	keras
	tensorflow


1. Collection data from social network
	Creat a Twitter account and get Token as well as Sercet key to using Streaming API
	create a folder /data/ in folder ./data_Collection
	Streaming run with:
	-python twitter_stream_download.py -q [namefile] -d data
	Copy json file to folder ./pre_time_eventDetection for Preprocessing step
	



2. Pre-process Json --> csv format, some pre processing
	Go to folder ./pre_time_eventDetection
	Convert Json to csv with consideration attribute [ID , text, creat_at....]
	-python earthquake2csv.py 
	Some preprocessing
	-python preprocessingSCV.py
	Copy output.csv file to folder ./twitter_DataPre/earthquake_data for Classification using CNN
	Note: We need consider 3 column [ID] [Text] [] --> rename to [item_id] [item] [label]  like Training dataset and Change name into newinput.csv (Label of input Tweet we collected here now empty)
	
	

3. Dataset and Preparing training/ test dataset for CNN
	The data output from previous phase is output.csv format with three columns (This is tweet we collect from social network) 
	Sameple.csv is earthquake related dataset we use for training and test CNN model (about 3464 tweets)
	Go outmost folder contain code
	Preprocess dataset
	-python helpers/preprocess.py twitter_DataPre/sample.csv
	-python helpers/split_data.py twitter_DataPre/sample_prccd.csv
	Copy all output file into folder .twitter_DataPre/earthquake_data and change name file coressponding


	  
4. Training a CNN model and Predict Informative tweet based on CNN model which already trained
	Folder embeddings/ includes word vector file from Google: (8Gb) and Glove focus on Twitter context (just 2Gb) I use this file
	-bash run_cnn.sh get the performance of CNN based model detailed on log file and Result predict (Informative / Not informative) on INPUTlabelPred.scv (see in original folder)
	-Edit file on Step 2 based on out put of classification to move to Time event detection



5. Time event detection
	Go to folder ./pre_time_eventDetection agian to accumulate occurence of keyword related tweet
	Run script
	-python accumulateTime.py
	Out put will be use to run Time event detection (Now this algorithm I code on Matlab--> you should run on matlab with input file.csv easily)


