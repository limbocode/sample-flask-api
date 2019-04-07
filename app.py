import os
import json
import pandas as pd
from flask import Flask, Response, abort, request

app = Flask(__name__)

# data = pd.read_csv('data/data.csv')
data = {
    '123': 100,
    '321': 1,
    '50': 98
}

@app.route('/update')
def item_update():
    if not request.json:
        abort(400)
    pk = request.json['pk']
    score = request.json['score']
    data[str(pk)] = int(score)

    return Response("pk " + str(pk) + " updated", status=200)


@app.route('/get/<int:pk>')
def item_score(pk):
    score = data[str(pk)]

    if score is None:
        abort(404)

    content = json.dumps({ 'pk': str(pk), 'score': str(score) })
    return Response(content, status=200, mimetype='applycation/json')

@app.route('/')
def sample():
    return 'Welcome to this sample app :)'


@app.errorhandler(404)
def not_found(e):
    return '', 404

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')