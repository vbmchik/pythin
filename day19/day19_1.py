from flask import Flask, jsonify, request, send_file

app = Flask("stat-bot")
@app.route('/stat-bot', methods=['GET'] )
def test():
    return 'Api works!'

@app.route('/api/v1/test', methods=['GET'])
def api_all():
    if 'id' in request.args:
        id = int(request.args["id"])
        return {"id": id, 'name': str(id) + ': the id'}
    return {'id': 200, 'name': 'test'}


app.run( port=5002)
