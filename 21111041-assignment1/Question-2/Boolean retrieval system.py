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


temp=open('posting_list.pkl',"rb")
plst=pickle.load(temp)

temp=open('file_index.pkl','rb')
file_index=pickle.load(temp)

temp=open('unique_tokens.pkl','rb')
dit=pickle.load(temp)


# In[3]:


q=input("Enter your query")
stop = set(stopwords.words('english'))
eachf=re.sub(r'[^\w\s]',' ',q)              #removing special characters
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
    if i not in stop:                         #removing stopwords 
        fin.append(i)


# In[4]:


#seperating operands and operators form the list
opt=[]
            
for i in range(len(fin)-1):
    opt.append("and")


# In[5]:


#creating boolean vector for each operand representing word present in that document index or not
boolmat=[]
mmat=[]
x=len(file_index)
tokn=set(dit.keys())
for i in fin:
    boolmat=[0]*x
    if i in tokn:
        for j in plst[i].keys():
            boolmat[j]=1
    mmat.append(boolmat)


# In[6]:


#taking AND operations on all the vectors from above
for i in opt:
    vector1=mmat[0]
    vector2=mmat[1]
    result=[b1&b2 for b1,b2 in zip(vector1,vector2)]
    mmat.pop(0)
    mmat.pop(0)
    mmat.insert(0,result)


# In[7]:


#printing document name satisfying above query
final_word_vector=mmat[0]
cnt=0
files=[]
for i in final_word_vector:
    if i==1:
        files.append(file_index[cnt])
    cnt+=1
files

