from bs4 import BeautifulSoup # to parse htlm
import codecs #to read the files
from nltk import word_tokenize # to separate into words
from nltk import FreqDist #to get frequencu table 
import os #to get fiel directory 
import glob #to get file directories at the same time 
import re #regular expressions
import csv #csv files 
import pandas as pd # to make data frames 



cwd = os.getcwd() #getting current directory 
files = glob.glob(cwd + '/*html') #getting all file names 

#result = []
FreqDistacc = FreqDist() #getting an empty FreqDst object

for file in files: 
	opener = codecs.open(file, "r", "utf-8") #opening all files
	soup = BeautifulSoup(opener, 'html.parser') #parsing the htlm files
	text = soup.get_text() #getting the text
	withoutHeader = text[text.find('www.easygerman.fm'):] #getting read of teh header
	withoutPunctiation = re.sub(r'[^\w\s]','',withoutHeader) #cleaning corpus 
	withoutNumbers = re.sub(r'[0-9]','',withoutPunctiation)
	withoutLink = withoutNumbers.replace('wwweasygermanfm', '')
	cleaned = withoutLink.replace('Cari', '')
	cleaned = cleaned.replace('Manuel', '')
	cleaned = cleaned.replace('Janusz', '')
	cleaned = cleaned.replace('Isi', '')
	words = word_tokenize(cleaned) #tokenezing cleaned corpus
	lowerCase = [each_string.lower() for each_string in words]
	FreqDistacc.update(lowerCase) #adding them to the freqDist object. 
	#result.append(fd)

sortedCounts = sorted(FreqDistacc.items() , key = lambda x: x[1] ,
                       reverse = True) #sortning them

dictionary = dict(sortedCounts) #turning it into a dictionary
print(len(dictionary))
df = pd.DataFrame.from_dict(dictionary, orient='index') #turning it into a data frame
#print(df)

df.to_csv('freqTable.txt', header=False, index=True, mode='a') #saving it 
