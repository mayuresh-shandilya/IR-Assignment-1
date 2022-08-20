#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
ps = PorterStemmer()
from collections import Counter
import pickle
import math
from num2words import num2words


# In[2]:


dit={}                                           #to store all unique words
fin_lst=[]                                       #to store all words of each file
tot_leng=[]                                      #to store length of each file 
stops = set(stopwords.words('english'))          #Taking all stopwords of english language in a list
path="english-corpora/"
files= os.listdir(path)
for txt in files:
    fls =path+txt    
    with open(fls, 'r',encoding='UTF-8') as f:
        eachf=f.read()  
        eachf=re.sub(r'[^\w\s]',' ',eachf)                  #removing punctuations from the strings 
        encoded_string = eachf.encode("ascii", "ignore")    #removing non ascii charachters
        eachf = encoded_string.decode()     
        tok=word_tokenize(eachf)                 #tokenizing all words in the particular document
        tok = [tk for tk in tok if len(tk)>1] 
        words=[]
        for t in tok:
            try:
                t=num2words(int(t))              #converting number to words 
            except:
                pass
            words.append(t)
        stem=[]
        for j in words:
            stem.append(ps.stem(j).lower())       #stematizing tokens
        lst=[]
        for i in stem:
            if i not in stops:                   #removing stopwords from list of tokens
                lst.append(i)                    #Making list containing all words of particular document
                if i not in dit:
                    dit[i]=0                     #creating dictionary of all unique
        tot_leng.append(len(lst))               #creating list of length of documents
        fin_lst.append(lst)                      #Making list of lists containing all words of particular document


# In[3]:


len(dit)


# In[4]:


path="english-corpora/"
files= os.listdir(path)
tf={}
df={}
for i in dit:
    tf[i]={}
    df[i]=0
for i in range(len(fin_lst)):
    count=Counter(fin_lst[i])                   #list containing word count of all words  
    for j in count.keys():
        df[j]+=1                                #calculating frequency of words
        tf[j][i]=count[j]                       #caculating dcoument frequency of words
         


# In[5]:


#calculating L2 norm 
L2_norm={}
m=0
for i in fin_lst:
    x=0
    for j in set(i):
        x+=(i.count(j)*math.log(len(files)/df[j]))**2   
    L2_norm[m]=(math.sqrt(x))
    m+=1


# In[6]:


with open('file_index.pkl','wb') as file:
    pickle.dump(files,file)
    file.close()

with open('unique_tokens.pkl','wb') as file:
    pickle.dump(dit,file)
    file.close()
    
with open('posting_list.pkl','wb') as file:
    pickle.dump(tf,file)
    file.close()
    
with open('document_frequency.pkl','wb') as file:
    pickle.dump(df,file)
    file.close()
    
with open('document_length.pkl','wb') as file:
    pickle.dump(tot_leng,file)
    file.close()
    
with open('Total_words.pkl','wb') as file:
    pickle.dump(fin_lst,file)
    file.close()
    
with open('L2_norm.pkl','wb') as file:
    pickle.dump(L2_norm,file)
    file.close()

