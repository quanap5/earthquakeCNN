# Earthquake detection using social media [here](http://sclab.cafe24.com/publications/581.pdf)

Twitter has become a potential data source to explore useful information mentioned  by  users. For instance, Twittertweets  related to an earthquake  will  be  utilized  to  detecttemporal  occurrence  as  wellas  location  information by a humanitarian organization. Therefore, we proposed a Convolution Neural Network (CNN) based method to determineinformative tweet and the real-time event detection algorithm to detect the timely occurrence of  the  given  event.  In  this  study, CNN model trained from the tweets related to the earthquake inthe past labeled by crowdsourcing plays a role as the classifierto predict an earthquake keyword related tweet is informativeor  not.  Then  these  informative  tweets  are  considered  as  input streaming data of time detection phase. Our system with the aid of  CNN  module  can  detect  the  earthquake  after it happens in the level of tolerance and ensure earlier than an announcementfrom official disaster website of government.

-Architecture
<img src="http://ieeexplore.ieee.org/document/7966735/figures">

----
## Getting Started

These below instructions will give you step by step command to run project

----
## Requirement

* Ubuntu
* python 2.7>
* keras
* tensorflow

----
## Running
### Collection data from social network
- creat a Twitter account and get Token as well as Sercet key to using Streaming API
- create a folder /data/ in folder ./data_Collection
- streaming run with
	- python twitter_stream_download.py -q [namefile] -d data
- Copy json file to folder ./pre_time_eventDetection for Preprocessing step
	
### Pre-process Json --> csv format, some pre processing
- go to folder ./pre_time_eventDetection
- convert Json to csv with consideration attribute [ID , text, creat_at....]
	- python earthquake2csv.py 
- Some preprocessing
	- python preprocessingSCV.py
- copy output.csv file to folder ./twitter_DataPre/earthquake_data for Classification using CNN
- Note: We need consider 3 column [ID] [Text] [] --> rename to [item_id] [item] [label]  like Training dataset and Change name into newinput.csv (Label of input Tweet we collected here now empty)	

### Dataset and Preparing training/ test dataset for CNN
- The data output from previous phase is output.csv format with three columns (This is tweet we collect from social network)
- Sameple.csv is earthquake related dataset we use for training and test CNN model (about 3464 tweets)
- Go outmost folder contain code
- Preprocess dataset
	- python helpers/preprocess.py twitter_DataPre/sample.csv
	- python helpers/split_data.py twitter_DataPre/sample_prccd.csv
- Copy all output file into folder .twitter_DataPre/earthquake_data and change name file coressponding
	  
### Training a CNN model and Predict Informative tweet
- Folder embeddings/ includes word vector file from Google: (8Gb) and Glove focus on Twitter context (just 2Gb) I use this file
- Run training:
	- bash run_cnn.sh get the performance of CNN based model detailed on log file and Result predict (Informative / Not informative) on INPUTlabelPred.scv (see in original folder)
</ul>
- Edit file on Step 2 based on out put of classification to move to Time event detection

### Time event detection
- Go to folder ./pre_time_eventDetection agian to accumulate occurence of keyword related tweet
- Run script:
	- python accumulateTime.py
- Out put will be use to run Time event detection (Now this algorithm I code on Matlab--> you should run on matlab with input file.csv)


