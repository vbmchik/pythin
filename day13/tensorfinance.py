import mysql.connector
import numpy
from keras import *
from keras import layers


incomesdb = mysql.connector.connect(
    host='localhost',
    user='python',
    password='!QA2ws3ed'
)

cursor = incomesdb.cursor()
query = 'select age, education_years, work_experience, country, salary_month from Predicator.incomes'
cursor.execute(query)
result = cursor.fetchall()

dataincomes = numpy.array(result)
input = dataincomes[0:8, 0:4]
output = dataincomes[0:8, 4]
print(dataincomes)

model = models.Sequential()
model.add(layers.Dense(units=16, input_shape=[4]))
model.add(layers.Dense(units=64))
model.add(layers.Dense(units=256))
model.add(layers.Dense(units=32))
model.add(layers.Dense(units=1))
model.compile(optimizer="adam", loss="mean_squared_error")
model.fit(x=input, y=output, epochs=5000)
tom = numpy.array([[18, 1, 1, 1]])
lisa = numpy.array([[52, 7, 20, 2]])
nik = numpy.array([[30, 3, 7, 1]])
kev = numpy.array([[30, 3, 7, 2]])
jjj = numpy.array([[30, 3, 7, 1], [30, 3, 7, 2]])
print(model.predict(jjj))

