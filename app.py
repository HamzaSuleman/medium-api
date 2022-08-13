from Diets import get_fullplan
from functions import get_ActiveDiet, get_Recommanded_Diets
from flask import Flask, jsonify, make_response
from Artificial_Intelligence.Recommander.recommander_test import tfidf_recommand


app = Flask(__name__)

plans = []
type = ['Weight_Loss_80kg','Bulking_Plan','Weight_Loss_65kg','Weight_Loss_Diabetes']
for x in type:
   plans.append(get_fullplan(x))

@app.route('/')
def get():
    response = make_response(jsonify(plans), 200)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/active-diet/<fname>/<lname>')
def get_active_data(fname, lname):
    activePlan = []
    activeDiet = get_ActiveDiet(type, fname+" "+lname)
    activePlan.append(activeDiet)
    response = make_response(jsonify(activePlan), 200)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/recommand/<category>/<disease>/<disease2>/')
def get_recommand_data(category, disease, disease2):

    recommanded_plans = []

    recommanded_diets = tfidf_recommand(category, disease, disease2)
    print(recommanded_diets)
    new_recommanded_diets = get_Recommanded_Diets(type, recommanded_diets)
    print(new_recommanded_diets)
    
    for x in new_recommanded_diets:
        recommanded_plans.append(get_fullplan(x))
    response = make_response(jsonify(recommanded_plans), 200)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__ == '__main__':
    app.run() 
