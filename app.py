from Diets import get_fullplan
from flask import Flask, jsonify, make_response

app = Flask(__name__)

plans = []
type = ['Weight_Loss_65kg','Bulking_Plan']
plans.append(get_fullplan(type[0]))
plans.append(get_fullplan(type[1]))


@app.route('/')
def get():
    response = make_response(jsonify(plans), 200)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__ == '__main__':
    app.run() 


