from Diets import get_fullplan
import ast
from functions import get_ActiveDiet, get_ActiveDiet_Total, get_Recommanded_Diets, get_TimeSeries_Values
from flask import Flask, jsonify, make_response
from Artificial_Intelligence.Recommander.recommander import tfidf_recommand


app = Flask(__name__)

plans = []
#type = ['Vegan_Weight_Loss60','Muscle_Gain_Diabetes','Bulking_80+']
type = ['Bulking_80+','Bulking_Plan','Muscle_Gain_Diabetes','Vegan_Weight_Loss60','Vegan_Weight_Loss80','Keto_Diet','Weight_Loss_65kg','Weight_Loss_80kg','Weight_Loss_100kg','Weight_Loss_Diabetes']
#type = ['Bulking_80+','Bulking_Plan','Muscle_Gain_Diabetes','Keto_Diet','Vegan_Weight_Loss60','Weight_Loss_65kg','Weight_Loss_80kg','Weight_Loss_Diabetes']


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


@app.route('/predictor/<startWeight>/<currentDay>/<fname>/<lname>/<weights>')
def get_predicted_weight_data(startWeight, currentDay, fname, lname, weights):
    
    activeDietName = (fname+" "+lname).strip()
    currentActiveDiet = get_ActiveDiet_Total(type, activeDietName)
    weights = ast.literal_eval(weights)
    #print(weights)
    #weights = [80.084757,80.173661,80.23,80.341101,80.4,80.45,80.647513,80.627513]
    TimeSeries = []
    TimeSeriesData = get_TimeSeries_Values(float(startWeight), int(currentDay), currentActiveDiet, list(weights))
    TimeSeries.append(TimeSeriesData)
    response = make_response(jsonify(TimeSeries), 200)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__ == '__main__':
    app.run() 
