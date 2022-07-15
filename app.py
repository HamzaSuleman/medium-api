from Diets import get_fullplan
from flask import Flask, jsonify, make_response

app = Flask(__name__)

plans = []
plans.append(get_fullplan('Bulking-Plan'))

@app.route('/')
def get():
    response = make_response(jsonify(plans), 200)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__ == '__main__':
    app.run() 

