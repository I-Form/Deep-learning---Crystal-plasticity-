import tensorflow as tf
from sklearn.model_selection import train_test_split
import numpy as np
from params import *
def loaddata():
    data1_file = [("./IPF_RGB.OriMap_%d.txt"%i) for i in range(NUM_OF_DATA)]
    data2_file = [("./phase_RGB.phase_%d.txt"%i) for i in range(NUM_OF_DATA)]
    IPF = np.empty((NUM_OF_DATA,1,100,100,3))
    Phase = np.empty((NUM_OF_DATA,1,100,100,3))
    #input_data = np.empty((NUM_OF_DATA,100,100,6))
    idx = 0
    for data1, data2 in zip(data1_file, data2_file):
        data1 = np.loadtxt(data1,delimiter=",")
        data1 = np.reshape(data1,(100,100,3))
        IPF[idx] = data1/255
        data2 = np.loadtxt(data2,delimiter=",")
        data2 = np.reshape(data2,(100,100,3))
        Phase[idx] = data2/255
        idx = idx + 1
    result = np.loadtxt("result.txt")
    result = np.reshape(result,(NUM_OF_DATA,1))
    #input_data = np.dstack((IPF, Phase))
    return Phase, IPF,result

class CNNModel(tf.keras.Model):
    def __init__(self):
        super(CNNModel, self).__init__()
        self.conv1_1 = tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(-1,100,100,3))
        self.maxpool1_1 = tf.keras.layers.MaxPool2D()
        self.conv1_2 = tf.keras.layers.Conv2D(64, (3,3), activation='relu')
        self.maxpool1_2 = tf.keras.layers.MaxPool2D()
        self.conv1_3 = tf.keras.layers.Conv2D(64, (3,3), activation='relu')
        self.flatten1_1 = tf.keras.layers.Flatten()
        self.dense1_1 = tf.keras.layers.Dense(32,activation='relu')

        self.conv2_1 = tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(-1,100,100,3))
        self.maxpool2_1 = tf.keras.layers.MaxPool2D()
        self.conv2_2 = tf.keras.layers.Conv2D(64, (3,3), activation='relu')
        self.maxpool2_2 = tf.keras.layers.MaxPool2D()
        self.conv2_3 = tf.keras.layers.Conv2D(64, (3,3), activation='relu')
        self.flatten2_1 = tf.keras.layers.Flatten()
        self.dense2_1 = tf.keras.layers.Dense(32,activation='relu')

        self.flatten3 = tf.keras.layers.Flatten()

        self.concat = tf.keras.layers.Concatenate()
        self.dense3_1 = tf.keras.layers.Dense(16,activation='relu')
        self.dense3_2 = tf.keras.layers.Dense(1,activation='sigmoid')


    def call(self, x1,x2):
        
        x1 = self.conv1_1(x1)
        x1 = self.maxpool1_1(x1)
        x1 = self.conv1_2(x1)
        x1 = self.maxpool1_1(x1)
        x1 = self.conv1_3(x1)
        x1 = self.flatten1_1(x1)

        
        x2 = self.conv2_1(x2)
        x2 = self.maxpool2_1(x2)
        x2 = self.conv2_2(x2)
        x2 = self.maxpool2_1(x2)
        x2 = self.conv2_3(x2)
        x2 = self.flatten2_1(x2)

        x = self.concat([x1,x2])
        x= self.flatten3(x)

        y = self.dense3_1(x)
        return self.dense3_2(y)

# Start
Phase, IPF,result = loaddata() #load data
inputdata = np.hstack((Phase, IPF)) #combine the two

x_train, x_test, y_train, y_test = train_test_split(inputdata, result, test_size=0.25, random_state=42) #randomly split train set & test set
train_ds = tf.data.Dataset.from_tensor_slices((x_train, y_train)).shuffle(10000).batch(32) 
test_ds = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(32)

model = CNNModel()

#print(model(np.random.rand(32,100,100,3),np.random.rand(32,100,100,3)))

loss_object = tf.keras.losses.MeanSquaredError()
optimizer = tf.keras.optimizers.Adam()

train_loss = tf.keras.metrics.Mean(name='train_loss')
train_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name='train_accuracy')
test_loss = tf.keras.metrics.Mean(name='test_loss')
test_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name='test_accuracy')

@tf.function
def train_step(images, labels):
  #images1 = np.reshape(images[0],(-1,100,100,3))
  #images2 = np.reshape(images[1],(-1,100,100,3))
  with tf.GradientTape() as tape:
    #print(np.shape(images),np.shape(images[:,0,:,:]),np.shape(images[:,0,:,:]))
    predictions = model(images[:,0,:,:],images[:,0,:,:])
    loss = loss_object(labels, predictions)
  gradients = tape.gradient(loss, model.trainable_variables)
  optimizer.apply_gradients(zip(gradients, model.trainable_variables))

  train_loss(loss)
  train_accuracy(labels, predictions)

@tf.function
def test_step(images, labels):
  #images1 = np.reshape(images[0],(-1,100,100,3))
  #images2 = np.reshape(images[1],(-1,100,100,3))
  predictions = model(images[:,0,:,:],images[:,0,:,:])
  t_loss = loss_object(labels, predictions)

  test_loss(t_loss)
  test_accuracy(labels, predictions)

EPOCHS = 5

for epoch in range(EPOCHS):

  train_loss.reset_states()
  train_accuracy.reset_states()
  test_loss.reset_states()
  test_accuracy.reset_states()

  for images, labels in train_ds:
    #print(np.shape(model(images)))
    #print(np.shape(labels))
    train_step(images, labels)

  for test_images, test_labels in test_ds:
    test_step(test_images, test_labels)

  template = 'Epoch {}, Loss: {}, Accuracy: {}, Test Loss: {}, Test Accuracy: {}'
  print (template.format(epoch+1,
                         train_loss.result(),
                         train_accuracy.result()*100,
                         test_loss.result(),
                         test_accuracy.result()*100))





