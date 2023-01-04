from tensorflow import *
from keras import *
from keras import layers


input = [1, 2, 3, 4, 5]
output = [3, 6, 9, 12, 15]
# creating neural network
model = models.Sequential()
# input layer
model.add(layers.Dense(units=5, input_shape=[1]))
# intermediate layer
model.add(layers.Dense(units=200, input_shape=[1]))
model.add(layers.Dense(units=1800, input_shape=[1]))
model.add(layers.Dense(units=320, input_shape=[1]))
model.add(layers.Dense(units=1, input_shape=[1]))


# model.compile(optimizer="adam",loss="mean_squared_error")
model.compile(optimizer="adam", loss="mse")

model.fit(x=input, y=output, epochs=500)

print(model.predict([11, 12]))