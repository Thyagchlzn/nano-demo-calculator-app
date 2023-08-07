from flask import Flask
import json 

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello'

@app.route("/calculator/add", methods=['POST'])
def add(number):
    return json.dumps({'result':number['first']+number['second']})

@app.route("/calculator/subtract", methods=['POST'])
def subtract(number):
    return json.dumps({'result':number['first']-number['second']})


if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
