import numpy as np
import csv
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('dataset.tsv', sep='\t',header=None,quoting=csv.QUOTE_NONE)
sentiment = np.array(data[2])

sentiment_dict = {}

for i in sentiment:
    if i not in sentiment_dict:
        sentiment_dict[i] = 1
    else:
        sentiment_dict[i] += 1

sentiment_classes = sorted(sentiment_dict.keys())
sentiment_classes_number = []

for i in sentiment_classes:
    sentiment_classes_number.append(sentiment_dict[i])

print(sentiment_classes)
print(sentiment_classes_number)
x = np.arange(len(sentiment_classes))

plt.xlabel('Sentiment Classes', fontsize = '14')
plt.ylabel('Number', fontsize = '12')
plt.title('Frequency distribution')
plt.bar(x,sentiment_classes_number, facecolor = '#9999ff', edgecolor = 'white')
plt.xticks(x,sentiment_classes,size='large')
for a,b in zip(x,sentiment_classes_number):
    plt.text(a,b+2,'%.0f' % b, ha='center', va='bottom')

plt.tight_layout()
plt.savefig('sentiment.png')
plt.show()

