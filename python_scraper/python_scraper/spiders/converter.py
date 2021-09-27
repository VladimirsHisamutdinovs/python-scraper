import pandas as pd
import os

data = pd.read_csv('dataset.csv', encoding='utf-8')
with open('dataset.txt', 'a+', encoding='utf-8') as f:
    for line in data.values:
        f.write((str(line[0])+'\t'+str(line[1])+'\n'))