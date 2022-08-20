#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
import re
import nltk
import pickle
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
ps = PorterStemmer()
import numpy as np
import math


# In[5]:


with open('file_index.pkl','rb') as file:
    file_no=pickle.load(file)
    file.close()
    
with open('posting_list.pkl','rb') as file:
    tf=pickle.load(file)
    file.close()
    
with open('document_frequency.pkl','rb') as file:
    df=pickle.load(file)
    file.close()
    
with open('document_length.pkl','rb') as file:
    doc_len=pickle.load(file)
    file.close()


# In[6]:


q=input("Enter your query")
stop = set(stopwords.words('english'))
eachf=re.sub(r'[^\w\s]',' ',q)           #removing special characters
encoded_string = eachf.encode("ascii", "ignore")    #removing non ascii charachters
eachf = encoded_string.decode()  
tok=word_tokenize(eachf)                      #tokenizing all words in the query
words=[]
for t in tok:
    try:
        t=num2words(int(t))              #converting number to words 
    except:
        pass
    words.append(t)
stem=[]
for j in tok:
    stem.append(ps.stem(j).lower())            #stematizing tokens
fin=[]
for i in stem:
    if i not in stop:                         #removing stop words
        fin.append(i)
avg=0
for i in range(len(doc_len)):                  #calculating average legth of all documents
    avg+=doc_len[i]
avg=avg/len(doc_len)

k=1.2
b=0.75
score={}
for i in range(len(file_no)):
    score[i]=0
    for j in fin:
        curtf=0
        curdf=0
        idf=0
        if j in tf:
            if i in tf[j]:
                curtf=tf[j][i]                 #retrieving term frequency from 
        if j in df:
            curdf=df[j]                        #retrieving document frequency from
            idf=math.log((len(file_no)-curdf+0.5)/(curdf+0.5)+1)
            score[i]+=idf*((k+1)*curtf/(curtf+k*(1-b+b*(doc_len[i]/avg))))

score=sorted(score.items(),key=lambda item: item[1],reverse=True)
x=0
for i in score:                                   #printing Top 10 files with highest score
    if x==10:
        break
    print(file_no[i[0]],i[1])
    x+=1


# In[ ]:




