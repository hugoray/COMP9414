import sys
import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import tree
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# open file
train_file = sys.argv[1]
test_file = sys.argv[2]

# read file
train_df = pd.read_csv(train_file, header=None, sep='\t')
test_df = pd.read_csv(test_file, header=None, sep='\t')

# extract two groups and ids
train_group = np.array(train_df[1])
test_group = np.array(test_df[1])
test_id = np.array(test_df[0])
y_train = np.array(train_df[2])
y_test = np.array(test_df[2])

analyser = SentimentIntensityAnalyzer()
predict_y = []
for text in test_group:
    score = analyser.polarity_scores(text)
    if score['compound'] >= 0.05:
        predict_y.append('positive')
    elif score['compound'] <= -0.05:
        predict_y.append('negative')
    else:
        predict_y.append('neutral')

print(classification_report(y_test,predict_y))
