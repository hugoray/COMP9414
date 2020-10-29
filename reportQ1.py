import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('dataset.tsv', sep='\t', header=None, quoting=csv.QUOTE_NONE)
sentiment = np.array(data[2])



# plot the distribution of sentiment
sentiment_dict = {}
for i in sentiment:
    if i not in sentiment_dict:
        sentiment_dict[i] = 1
    else:
        sentiment_dict[i] += 1

sentiment_classes = sorted(sentiment_dict.keys())
sentiment_classes_number = []
for c in sentiment_classes:
    sentiment_classes_number.append(sentiment_dict[c])
print(sentiment_classes)
print(sentiment_classes_number)
x = np.arange(len(sentiment_classes))

plt.xlabel('sentiment')
plt.ylabel('number')
plt.title('The occurrence of number of every sentiment')
plt.bar(x, sentiment_classes_number)
plt.xticks(x, sentiment_classes, size='large')
for a, b in zip(x, sentiment_classes_number):
    plt.text(a, b+0.05, '%.0f' % b, ha='center', va='bottom', fontsize=10)
plt.tight_layout()
plt.savefig('sentiment.png')
plt.show()
