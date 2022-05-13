import tensorflow as tf
from sklearn.model_selection import train_test_split
import numpy as np
from params import *
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
from tqdm import tqdm

import pydot
def loaddata():
    data1_file = [("./Input_05/IPF_RGB.OriMap_%d.txt"%i) for i in range(NUM_OF_DATA)]
    data2_file = [("./Input_05/phase_RGB.phase_%d.txt"%i) for i in range(NUM_OF_DATA)]
    data3_file = [("./Input_20/IPF_RGB.OriMap_%d.txt"%i) for i in range(NUM_OF_DATA)]
    data4_file = [("./Input_20/phase_RGB.phase_%d.txt"%i) for i in range(NUM_OF_DATA)]
    data5_file = [("./Input_50/IPF_RGB.OriMap_%d.txt"%i) for i in range(NUM_OF_DATA)]
    data6_file = [("./Input_50/phase_RGB.phase_%d.txt"%i) for i in range(NUM_OF_DATA)]
    data7_file = [("./Input_80/IPF_RGB.OriMap_%d.txt"%i) for i in range(NUM_OF_DATA)]
    data8_file = [("./Input_80/phase_RGB.phase_%d.txt"%i) for i in range(NUM_OF_DATA)]
    data9_file = [("./Input_95/IPF_RGB.OriMap_%d.txt"%i) for i in range(NUM_OF_DATA)]
    data10_file = [("./Input_95/phase_RGB.phase_%d.txt"%i) for i in range(NUM_OF_DATA)]
    data = np.empty((1000,100,100,3))

    idx = 0
    for data1, data2 in zip(data1_file, data2_file):
        data1 = np.loadtxt(data1,delimiter=",")
        data1 = np.reshape(data1, (100,100,3))
        data2 = np.loadtxt(data2, delimiter=",")
        data2 = np.reshape(data2, (100, 100, 3))
        data_tmp = data1 + data2
        data[idx] = data_tmp/255
        idx = idx + 1

    for data3, data4 in zip(data3_file, data4_file):
        data3 = np.loadtxt(data3,delimiter=",")
        data3 = np.reshape(data3, (100,100,3))
        data4 = np.loadtxt(data4, delimiter=",")
        data4 = np.reshape(data4, (100, 100, 3))
        data_tmp = data3 + data4
        data[idx] = data_tmp/255
        idx = idx + 1

    for data5, data6 in zip(data5_file, data6_file):
        data5 = np.loadtxt(data5,delimiter=",")
        data5 = np.reshape(data5, (100,100,3))
        data6 = np.loadtxt(data6, delimiter=",")
        data6 = np.reshape(data6, (100, 100, 3))
        data_tmp = data5 + data6
        data[idx] = data_tmp/255
        idx = idx + 1   

    for data7, data8 in zip(data7_file, data8_file):
        data7 = np.loadtxt(data7,delimiter=",")
        data7 = np.reshape(data7, (100,100,3))
        data8 = np.loadtxt(data8, delimiter=",")
        data8 = np.reshape(data8, (100, 100, 3))
        data_tmp = data7 + data8
        data[idx] = data_tmp/255
        idx = idx + 1  

    for data9, data10 in zip(data9_file, data10_file):
        data9 = np.loadtxt(data9,delimiter=",")
        data9 = np.reshape(data9, (100,100,3))
        data10 = np.loadtxt(data10, delimiter=",")
        data10 = np.reshape(data10, (100, 100, 3))
        data_tmp = data9 + data10
        data[idx] = data_tmp/255
        idx = idx + 1

    result_file = ['YieldStress_05.txt', 'YieldStress_20.txt', 'YieldStress_50.txt', 'YieldStress_80.txt',
                   'YieldStress_95.txt']
    result = np.zeros((1000,1))
    idx = 0
    for file in result_file:
        result[idx:idx+200,:] = np.reshape(np.loadtxt(file),(200,1))
        idx += 200



    return data,result
# #combine the two
data, result = loaddata()
x_train, x_test, y_train, y_test = train_test_split(data, result, test_size=0.25, random_state=42) #randomly split train set & test set
train_ds = tf.data.Dataset.from_tensor_slices((x_train, y_train)).shuffle(10000).batch(32)
test_ds = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(32)
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(100, 100, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(1))
model.compile(optimizer='adam',
              loss=tf.keras.losses.MeanAbsolutePercentageError(),
              metrics=[tf.keras.metrics.MeanAbsolutePercentageError()])

history = model.fit(train_ds, epochs=1,
                    validation_data=test_ds)
model.save("model_before.h5")
y_pred = model(x_test)
y_true = y_test

residual = abs(y_true - y_pred) / y_true
print(residual)
np.savetxt("./resi/residual_model2_10.csv", residual)


