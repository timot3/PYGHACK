from sklearn.ensemble import RandomForestRegressor

import data_extraction as data
import numpy as np
import math
import matplotlib.pyplot as plt

DATA_FILE = 'data.txt'
NUM_ROWS = 30
TRAIN_VALIDATION_SPLIT = 0.95
#np.random.seed(3)

def RMSE(x, y):
    acc = 0
    for i in range(len(x)):
        acc = acc + (x[i] - y[i])**2
    return math.sqrt(acc / len(x))

print("Loading in Data")
labels, features = data.extract_data_from_file(DATA_FILE, NUM_ROWS)
#perm = np.random.permutation(len(labels))
#features = features[perm].numpy()
#labels = labels[perm].numpy()
#
#xtrain = features[:int(len(features) * TRAIN_VALIDATION_SPLIT), :]
#ytrain = labels[:int(len(features) * TRAIN_VALIDATION_SPLIT)]
#
#xval = features[int(len(features) * TRAIN_VALIDATION_SPLIT):, :]
#yval = labels[int(len(features) * TRAIN_VALIDATION_SPLIT):]

clf = RandomForestRegressor(n_estimators=50)

print("Initializing Training")
clf.fit(features, labels)

plt.bar([i for i in range(1, 9)], clf.feature_importances_)


#y_pred = clf.predict(xval)
#
#acc = RMSE(y_pred, yval)
#
#print("Model Accuracy: ", acc)

#print(clf.predict([[2.3,16631,15.7,44638,77991,59.7]]))
