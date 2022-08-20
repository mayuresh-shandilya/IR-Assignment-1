#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[2]:


with open('document_frequency.pkl','rb') as file:
    df=pickle.load(file)
    file.close()
    
with open('file_index.pkl','rb') as file:
    file_no=pickle.load(file)
    file.close()
    
with open('Total_words.pkl','rb') as file:
    total_words=pickle.load(file)
    file.close()
    
with open('L2_norm.pkl','rb') as file:
    l2_norm=pickle.load(file)
    file.close()


# In[3]:


q=input("Enter your query")
stop = set(stopwords.words('english'))
eachf=re.sub(r'[^\w\s]',' ',q)             #removing special characters
encoded_string = eachf.encode("ascii", "ignore")    #removing non ascii charachters
eachf = encoded_string.decode()  
tok=word_tokenize(eachf)                       #tokenizing all words in the query
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
    if i not in stop:                          #removing stopwords 
        if i in df.keys():                     #cheaking if word present in unique keys
            fin.append(i)

lst=[]
x=0
for i in fin:
    tf_idf=(fin.count(i)*math.log(len(file_no)/df[i]))    #buliding query vector
    lst.append(tf_idf)
    x+=tf_idf**2
x=math.sqrt(x)
lst1=np.array(lst)/x


score={}
for i in range(len(file_no)):
    k=[]
    for j in fin:
        tf_idf=(total_words[i].count(j)*math.log(len(file_no)/df[j]))         #building document vector 
        k.append(tf_idf)
    k=np.array(k)/l2_norm[i]
    score[i]=np.dot(lst1,k)

score=sorted(score.items(),key=lambda x:x[1],reverse=True)


# In[4]:


x=0
for i in score:
    if x==10:
        break
    print(file_no[i[0]],i[1])
    x+=1


# In[ ]:





# In[ ]:




