import pandas as pd
from Diets import get_fullplan

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
    
   