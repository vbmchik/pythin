import mysql.connector

class fileOperator():

    def __init__(self, host, user, password, query=''):
        # вы добавите исключение если такой базы нет или ошибка авторизации (исключения пайтон)
        # к тому же хост пользователь и пароль запмоните в этом классе
        #self.error=false
        self.user=user
        self.dbase = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        self.query=query
        self.cursor = self.dbase.cursor()
  
    def setQuery(self, query):
            self.query=query
            return self
    
    def getData(self):
        if self.query =='':
            return []
        self.cursor.execute(self.query)
        return self.cursor.fetchall()

