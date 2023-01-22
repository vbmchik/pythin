# -*- coding: utf-8 -*-
from flask import Flask, request, json, Response
from dbFile import DataHelp


app = Flask(__name__)

#     Пользователь обращается к API
#     1 получение всех данных
#     2 получение данных какого то года
#     3 получение данных года и месяца
#     4 данные какого то бизнеса
#     5 мы создаем метод который будет использовать все эти параметры

app = Flask('API_1')
app.config['JSON_AS_ASCII'] = False
d = DataHelp()
@app.route('/', methods=['GET'])
def test():
    return 'Hello!!! I am working!!!'
@app.route('/api/v1/search', methods=['GET'])
def search():
    if 'id' in request.args:
        id = int(request.args["id"])
        return {"id":id, "name": str(id)+': the is'}
    return {'id': 200, 'name': 'test'}


@app.route('/api/v1/income', methods=['GET'])
def incomes():
    year=-1
    month=""
    business=""
    if 'year' in request.args:
        year = int(request.args["year"])
    if "month" in request.args:
        month = request.args["month"]
    if "business" in request.args:
        business = request.args["business"]
    query = "select year, month, business.name as business, income from Predicator.Finances left join Predicator.business on business.id=business"
    notfirst = False
    # where year = 2323 and month = "ddf" and 
    if year != -1 or month != "" or business != "":
       query = query + " where "
       for arg in request.args:
            if arg != "year" and arg != "month" and arg != "business":
               continue
            if notfirst:
                query = query + " and "
            s = request.args[arg]
            if arg == "year":
                query = query + f" year = {s}"
            if arg == "month":
                query = query + f" month = '{s}'"
            if arg == "business":
                   query = query + f" business.name = '{s}'"
            notfirst = True   
    response = Response(
        json.dumps(d.executeSomeQuery(query)), content_type="application/json; charset=utf-8")
    return response
app.run()