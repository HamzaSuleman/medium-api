import pandas as pd
from Diets import get_fullplan
from Artificial_Intelligence.Predictor.Predictor import TimeSeriesAlgorithm

def get_ActiveDiet(Diets, activeDietName):

    for diet in Diets:
        Plan = pd.read_csv('Diet-Plans/'+diet+'/'+diet+'.csv')
        Total = pd.read_csv('Diet-Plans/'+diet+'/Total.csv')
        if(Plan['Plan Name'].loc[0] == activeDietName):
            return get_fullplan(diet)
    else:
        return {
            'name': 'Name',
            'image':'Image',
            'total_plan_calories_consume': 0,
            'total_plan_calories_burn': 0,
            'days': []
            }

def get_Recommanded_Diets(Diets, recommandedDietList):

    recommand_plans = []
    for diet in Diets:
        Plan = pd.read_csv('Diet-Plans/'+diet+'/'+diet+'.csv')
        for i in range(len(recommandedDietList)):
            if(str(Plan['Plan Name'].loc[0]).strip() == recommandedDietList[i]):
                recommand_plans.append(diet)
    return recommand_plans

def get_TimeSeries_Values(startWeight, currentDay, activeDietName, weights):

    Weights = TimeSeriesAlgorithm(startWeight, currentDay, activeDietName, weights)
    return Weights

def get_ActiveDiet_Total(Diets, activeDietName):
    realActiveDietName = ''

    for diet in Diets:
        Plan = pd.read_csv('Diet-Plans/'+diet+'/'+diet+'.csv')
        if(Plan['Plan Name'].loc[0] == activeDietName):
            realActiveDietName = diet

    currentDiet = pd.read_csv("Diet-Plans/"+realActiveDietName+"/Total.csv")
    return currentDiet