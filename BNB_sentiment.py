import sys
import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

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


def legalization(raw):
    return_list = []
    for line in raw:
        # url remove rule from stackoverflow
        url_remove = re.sub(r'(http|https)://[a-zA-Z0-9.?/&=:]*', ' ', line)
        # junk character remove
        char_remove = re.sub(r'[^#@_$%\w\d\s]', '', url_remove)
        return_list.append(char_remove)

    return return_list

legal_train_group = np.array(legalization(train_group))
legal_test_group = np.array((legalization(test_group)))

# use sklearn's countvectorizer to legalize two groups
count = CountVectorizer(token_pattern='[#@_$%\w\d]{2,}',lowercase=False)

X_train_bag_of_words = count.fit_transform(legal_train_group)
X_test_bag_of_words = count.transform(legal_test_group)

# BNB
clf = BernoulliNB()
bnb_model = clf.fit(X_train_bag_of_words, y_train)
predicted_y = bnb_model.predict(X_test_bag_of_words)
#print(classification_report(y_test, predicted_y))
for i in range(len(test_group)):
    print(test_id[i],predicted_y[i])