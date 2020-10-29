import pandas as pd
import numpy as np

file_name = 'dataset.tsv'
train_data = pd.read_csv(file_name, sep = '\t', header = None, nrows=4000)
train_data.to_csv('training.tsv',sep = '\t',header= None, index=False)

test_data = pd.read_csv(file_name, sep = '\t', header = None, skiprows=4000)
test_data.to_csv('test.tsv',sep = '\t',header = None, index = False)
