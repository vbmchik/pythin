from keras import*
from tensorflow import *
#
#model=Sequential()

#model.add(layers.Dense(units=12,input_shape=[1]))

#model.add(layers.Dense(units=8,input_shape=[1]))

#model.add(layers.Dense(units=1,input_shape=[1]))
input_list = [1, 2, 3, 4, 5, 6, 7, 8]
output_list = [3, 6, 9, 12, 15, 18, 21, 24]

#model.compile(loss='mean_squared_error',optimizer='adam')

#model.fit(x=input_list,y=output_list,epochs=10000)

#model.save('tensor1')
model = models.load_model('tensor1')
print(model.predict([9]))
print(model.predict([12]))
print(model.predict([22]))
print(model.predict([200]))
print(model.predict([1001]))
