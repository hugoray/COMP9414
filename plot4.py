import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))

plt.axis([-0.4, 4.8, 0, 1.0])
label_list = ['BNB','MNB','DT','VADER','MINE']
accuracy = [0.73,0.76,0.71,0.54,0.81]
macro_avg = [0.55,0.64,0.60,0.51,0.74]

x = np.arange(len(label_list))
#plt.xlabel('Sentiment Classes', fontsize = '14')

width = 0.35

rects1 = plt.bar(x, accuracy, alpha = 0.6, width=width, label='accuracy',facecolor = 'deeppink', edgecolor = 'grey')
rects2 = plt.bar(x + width, macro_avg, alpha = 0.8,width=width, label='macro_avg',facecolor = '#9999ff', edgecolor = 'grey')
plt.legend(loc= 'upper right')
plt.yticks(np.arange(0, 1.1, 0.1))
#plt.ylabel('Value',size = 'large')
plt.xticks([index + 0.15 for index in x], label_list,size = 'large')
plt.title('Comparison on accuracy and macro-average')
# 编辑文本
plt.hlines(0.81, -0.4, 4.15,alpha = 0.2,color= 'grey', linestyles = 'dashed')
plt.hlines(0.74, -0.4, 4.5,alpha = 0.2,color= 'grey', linestyles = 'dashed')
for rect in rects1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
for rect in rects2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")

plt.savefig('1.png')
plt.show()
