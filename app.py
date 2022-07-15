from Diets import get_fullplan
from flask import Flask, jsonify, make_response

app = Flask(__name__)

plans = {}
type = ['Bulking-Plan']
plans['Paklife '+type[0]] = get_fullplan(type[0])

@app.route('/')
def get():
    response = make_response(jsonify(plans), 200)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__ == '__main__':
    app.run() 

