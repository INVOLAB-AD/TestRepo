# TEST-1

**Environment setup:**
1. Install instapy `pip3 install instapy`
2. Install Mozilla Firefox for selenium [click to download](https://www.mozilla.org/en-US/firefox/new/)
3. Install facebook-sdk `pip3 install facebook-sdk`
4. register on [https://developers.facebook.com/](https://developers.facebook.com/) for ACCESS KEY
 - register on the above link
 - create an APP with any APP NAME ex: TESTAPP
 - click on **tools** on navbar above and then click on **Graph API Explorer**
 - CLICK on the dropdown below the app name and click on *Get User Access Token*
 - Copy The ACCESS Token and paste in the code in file **facebook_test.py**

**Sentiment Analysis:**
1. Scrape Youtube comments with the help of selenium follow procedures from [this link](https://towardsdatascience.com/how-to-scrape-youtube-comments-with-python-61ff197115d4)
 
 or
 
Use Youtube comment datasets from [this link](https://www.kaggle.com/datasnaek/youtube?select=GBcomments.csv)
 
2. Now Do opinion mining with the help of nltk in python and read data using pandas module follow procedures from [this link](https://towardsdatascience.com/using-nlp-to-figure-out-what-people-really-think-e1d10d98e491)
  - Cleaning the data
  - Analyzing data
 
**Deception Detection:**
1. Deception detection is a method to detect lie in comments or reviews.
2. Deception Detection using python and NLTK can be done by following procedures on [this link](https://www.datacamp.com/community/tutorials/machine-learning-hotel-reviews)
 - Import Modules
 ```
 import os
 import fnmatch
 from textblob import TextBlob
 import pandas as pd
 from sklearn.feature_extraction.text import TfidfVectorizer
 from nltk.corpus import stopwords
 from nltk import pos_tag,pos_tag_sents
 import regex as re
 import operator
 from sklearn.svm import SVC, LinearSVC
 from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
 from sklearn.cross_validation import train_test_split  
 from sklearn import metrics
 from sklearn import svm
 from sklearn.grid_search import GridSearchCV
 import pickle
 from nltk.corpus import stopwords
 ```
 - Fetch all text files from the path and extract the labels from it and create a dataframe of the labels
 - Fetch all the reviews and append in a list
 - Merge the review dataframe and label dataframe
 - Remove stopwords from the Hotel Reviews column
 - Extract parts of speech from Hotel Reviews which will be fed as a Feature Input to the model
 - Training Phase:
  * Split the Data into two parts 80% train and 20% test data
  * Implementing the Model
  * Predict on the Test Data
  * Plot the confusion matrix, accuracy score and the classification report to analyse the performance of the model
  * Test the Model using different Random States
  * Test the model with two reviews from Yelp

**"Main Gunda Mawali Ya eve teaser nahi!"**

**Note:**
The model's performance varies when implemented on a different processing system having different specifications, this is an unusual behavior observed. If the community can help figure out this problem, it would help a lot of people including the author of this post. By community, it means the readers who will go through this tutorial!*
