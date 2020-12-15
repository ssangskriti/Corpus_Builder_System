In this corpus builder system comments of the posts from the official facebook page of bKash Limited are used as the dataset.
The comments were crawled using **facepager** from here https://github.com/strohne/Facepager/releases. The crawled dataset can be found in _bkash_comments.csv_ file.

FastText has been used to extract the bengali comments. _bangla_comments_separator.ipynb_ file extracts the bengali comments out of the csv file. 

In the _comments_classifier.ipynb_ gile, I removed the rows with
NULL values and I ran a KNN algorithm on the data with the value of K as 3. This algorithm classifies the most 
similar words together. Next, I checked in each line how many words are from which class. Counted the number of 
words from each class and distributed the lines as a member of those classes. Finally put all the lines in a dictionary and 
dumped it into the _classified_comments.json_ file.