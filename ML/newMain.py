# #!/usr/bin/env python
# import csv
#
# #f = open('files/input.csv', newline='')
#
# f = open('/var/www/html/files/input.csv', newline='')
# reader = csv.reader(f)
# row1 = next(reader)
# str = ""
# for i in range(0, 10):
#     str += row1[i] + ", "
# str += row1[10]
# print(str)
#
# #print("2, 11, 14, 23, 8, 4, 16, 7, 2, 5, 3")

from sklearn.ensemble import RandomForestRegressor
import numpy as np
import math
import matplotlib.pyplot as plt

import torch

def extract_data_from_file(file, num_rows):
    list_data = []
    with open(file, 'r', encoding="utf-8") as fin:
        line = fin.readline()
        counter = 1
        while line:
            try:
                temp = line.split(',')[2:]
#                temp[-1] = temp[-1][:-1]
                list_data.append(list(map(float, temp)))
            except:
                counter = counter
#            if counter % 1000 == 0:
#                print("%.2f%% Finished" % (counter / num_rows * 100))

            line = fin.readline()
            counter = counter + 1
    raw_data = torch.as_tensor(list_data).float()
#    print(raw_data.shape)
    labels = raw_data[:,-1]
    features = raw_data[:,:-1]

    return (labels, features)

def normalize(x):
    return (x - x.mean()) / x.std()

DATA_FILE = '/var/www/html/files/input.csv'
NUM_ROWS = 29569
TRAIN_VALIDATION_SPLIT = 0.95
#np.random.seed(3)

def RMSE(x, y):
    acc = 0
    for i in range(len(x)):
        acc = acc + (x[i] - y[i])**2
    return math.sqrt(acc / len(x))

#print("Loading in Data")
labels, features = extract_data_from_file(DATA_FILE, NUM_ROWS)
#perm = np.random.permutation(len(labels))
#features = features[perm].numpy()
#labels = labels[perm].numpy()
#
#xtrain = features[:int(len(features) * TRAIN_VALIDATION_SPLIT), :]
#ytrain = labels[:int(len(features) * TRAIN_VALIDATION_SPLIT)]
#
#xval = features[int(len(features) * TRAIN_VALIDATION_SPLIT):, :]
#yval = labels[int(len(features) * TRAIN_VALIDATION_SPLIT):]

clf = RandomForestRegressor(n_estimators=50,)

#print("Initializing Training")
clf.fit(features, labels)

print(*(clf.feature_importances_ * 100))


#y_pred = clf.predict(xval)

#acc = RMSE(y_pred, yval)

#print("Model Accuracy: ", acc)

#print(clf.predict([[2.3,16631,15.7,44638,77991,59.7]]))
