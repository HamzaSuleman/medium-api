from Diets import get_fullplan
from ActiveDiet import get_ActiveDiet
from flask import Flask, jsonify, make_response

app = Flask(__name__)

plans = []
type = ['Weight_Loss_80kg','Weight_Loss_65kg','Bulking_Plan','Weight_Loss_Diabetes']
for x in type:
   plans.append(get_fullplan(x))

@app.route('/')
def get():
    response = make_response(jsonify(plans), 200)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/active-diet/<fname>/<lname>')
def get_data(fname, lname):
    activePlan = []
    activeDiet = get_ActiveDiet(type, fname+" "+lname)
    activePlan.append(activeDiet)
    response = make_response(jsonify(activePlan), 200)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__ == '__main__':
    app.run() 
