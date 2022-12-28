from findict import Finance

host='localhost'
user='python'
password='!QA2ws3ed'

finobject = Finance(host, user, password, 'Predicator', 'Finances')

print(finobject.d)