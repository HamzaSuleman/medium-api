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


def get_Recommanded_Diets2(Diets, recommandedDietList):

    recommand_plans = []

    print(Diets)
    for j in range(len(Diets)):
        name = str(Diets[j])

        Plan = pd.read_csv('Diet-Plans/'+name+'/'+name+'.csv')
        for i in range(0,len(recommandedDietList)):
            if(Plan['Plan Name'].loc[0] == recommandedDietList[i]):
                print(recommandedDietList[i])
                recommand_plans.append(j)
                print(recommand_plans)
    
    return recommand_plans

def get_Recommanded_Diets(Diets, recommandedDietList):

    recommand_plans = []
    for diet in Diets:
        Plan = pd.read_csv('Diet-Plans/'+diet+'/'+diet+'.csv')
        for i in range(len(recommandedDietList)):
            if(str(Plan['Plan Name'].loc[0]).strip() == recommandedDietList[i]):
                recommand_plans.append(diet)
    return recommand_plans