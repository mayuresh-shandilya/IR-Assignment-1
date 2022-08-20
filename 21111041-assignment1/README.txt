CS657A: Information Retrieval
Assignment 1.

Directory :
"21111041-qrels.zip", "21111041-ir-systems.zip", one Makefile ,english-corpora and one README file.

(A)The "21111041-qrels.zip" file contains two files which are asked in question 3,
   (1) Queries.txt - It contains a set of 20 queries, each in one single line.The first field of a query line is the query id (from Q01 to Q20).
      The second field is a free text. The fields are separated by a TAB character.

   (2)QRels_BM25.csv - It contains a set of 20 relevant documents for each query in the "Queries.txt" file in the following QRels format.

(B)The "21111041-ir-systems.zip" file contains the following files:
   (1)Boolean retrieval system.py - It is the code which implements the simple Boolean Retrieval System.
   (2)TF_IDF.py - It is the code which implements a system from the TFIDF family.
   (3)BM25.py - It is the code which implements a system from the BM25 family.
   (4)test.sh - It is the shell script which is run by the Makefile to run all the three systems.
   (5)pkl files - These files contain the data structures which store the data required to run the three systems like Posting List of words,
      Length of each document, Document Frequency (DF) for each word etc.      

(C)Makefile - It runs all the three systems by invoking the "test.sh" file in the "21111041-ir-systems.zip" file for the query file that is given  
   as the parameter when running this Makefile .

How to run the Makefile to execute all the three systems:
To run this file in terminal run command :-    make run filename=Queries    here Queries id the name of file you provide.

This Makefile unzips the "21111041-ir-systems.zip" file and runs the "test.sh" file present in that file and all the three systems will run on the provided queries
the outputs is genrated  in CSV format in the same directory where this Makefile is present. The input query file should be present in the same directory where the Makefile is present.

The Boolean retrieval system.py file will generate QRels_BRS.csv as the output.
The TF_IDF.py file will generate QRels_TF_IDF.csv as the output.
The BM25.py file will generate QRels_BM25.csv as the output.
Each of the output files will contain a set of 10 relevant documents for each query in the QRels format.
