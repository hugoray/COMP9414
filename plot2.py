import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6,5))
label_list = ['BNB','MNB']
num_list_1 = [0.78,0.79]
num_list_2 = [0.73,0.76]

x = np.arange(len(num_list_1))
#plt.xlabel('Sentiment Classes', fontsize = '14')

width = 0.35

rects1 = plt.bar(x, num_list_1, alpha = 0.6, width=width, label='1000-word',facecolor = 'deeppink', edgecolor = 'white')
rects2 = plt.bar(x + width, num_list_2, alpha = 0.8,width=width, label='whole-vocabulary',facecolor = '#9999ff', edgecolor = 'white')
plt.legend(loc= 'upper right')
plt.yticks(np.arange(0, 1.1, 0.1))
plt.ylabel('Accuracy',size = 'large')
plt.xticks([index + 0.15 for index in x], label_list,size = 'large')
plt.title('Comparison on accuracy between two models')
# 编辑文本

for rect in rects1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
for rect in rects2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")

plt.savefig('1.png')
plt.show()
