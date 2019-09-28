import csv
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

train_X = np.zeros((30, 6))
train_Y = np.zeros((30, 1))
data = np.zeros((30, 7))

with open("data.csv") as csv_file:
    
    csv_reader = csv.reader(csv_file, delimiter = ",")
    line_count = -1
    
    for row in csv_reader:
        
        line_count += 1
        
        if(line_count == 0):
            continue
        
        data[line_count - 1] = row[1:]

permutation = np.random.permutation(30)

train_X = data[:, :6]
train_Y = data[:, 6]

train_X = train_X[permutation]
train_Y = train_Y[permutation]

validation_X = train_X[24:]
validation_Y = train_Y[24:]

regressor = RandomForestRegressor(n_estimators = 10)
regressor.fit(train_X, train_Y)

error = 0

for i in range(6):
    predicted = regressor.predict(validation_X[i].reshape(1, -1))
    actual = validation_Y[i]
    error += (predicted - actual) ** 2

error /= 6
error =  error ** 0.5
print(error)
