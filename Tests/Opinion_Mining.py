# applying scrape comments algorithm
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

data=[]
with Chrome() as driver:
    wait = WebDriverWait(driver,15)
    driver.get("https://www.youtube.com/watch?v=kuhhT_cBtFU&t=2s")
for item in range(200): 
        wait.until(EC.visibility_of_element_located((By.TAG_NAME,"body"))).send_keys(Keys.END)
        time.sleep(15)
for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content-text"))):
        data.append(comment.text)

import pandas as pd   
df = pd.DataFrame(data, columns=['comment'])
df.head()


# Applying Opinion Mining algorithm using Natural Language Processing (using NLTK)

#Import packages
import pandas as pd
import re, string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer 
from textblob import TextBlob
sw = stopwords.words('english')

#The function for data cleaning

def clean_text(text):
  text = text.lower()
  text = re.sub('@', '', text)
  text = re.sub('\[.*?\]', '', text)
  text = re.sub('https?://\S+|www\.\S+', '', text)
  text = re.sub('<.*?>+', '', text)
  text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
  text = re.sub('\n', '', text)
  text = re.sub('\w*\d\w*', '', text)
  text = re.sub(r"[^a-zA-Z ]+", "", text)
    
  #Tokenize the data
  text = nltk.word_tokenize(text)
  #Remove stopwords
  text = [w for w in text if w not in sw]
  return text

# applying comment to each comment using lambda function and clean_text
df['comment'] = df['comment'].apply(lambda x: clean_text(x))

#Lemmatizer use this link to know about Lemmatization (https://www.geeksforgeeks.org/python-lemmatization-with-nltk/)
lemmatizer = WordNetLemmatizer()
def lem(text):
    text = [lemmatizer.lemmatize(t) for t in text]
    text = [lemmatizer.lemmatize(t, 'v') for t in text]
    return text
df['comment'] = df['comment'].apply(lambda x: lem(x))

#Remove all empty comments
empty_comment = df['comment'][1459]
for i in range(len(df)):
    if df['comment'][i]==empty_comment:
        df=df.drop(i)
df=df.reset_index(drop=True)

#From lists of comments to a single list containing all words      
all_words=[]        
for i in range(len(df)):
    all_words = all_words + df['comment'][i]
#Get word frequency        
nlp_words = nltk.FreqDist(all_words)
plot1 = nlp_words.plot(20, color='salmon', title='Word Frequency')

#Bigrams
bigrm = list(nltk.bigrams(all_words))
words_2 = nltk.FreqDist(bigrm)
words_2.plot(20, color='salmon', title='Bigram Frequency')

#Get sentiment from comments
df['comment'] = [str(thing) for thing in df['comment']]
sentiment = []
for i in range(len(df)):
    blob = TextBlob(df['comment'][i])
    for sentence in blob.sentences:
        sentiment.append(sentence.sentiment.polarity)
df['sentiment']=sentiment
#Plot
df['sentiment'].plot.hist(color='salmon', title='Comments Polarity')
