import pandas as pd

def get_plan(planFileName):
    #Calling Data From excel
    Breakfast = pd.read_csv('Diet-Plans/'+planFileName+'/Breakfast.csv')
    Snack1 = pd.read_csv('Diet-Plans/'+planFileName+'/Snack1.csv')
    Lunch = pd.read_csv('Diet-Plans/'+planFileName+'/Lunch.csv')
    Snack2 = pd.read_csv('Diet-Plans/'+planFileName+'/Snack2.csv')
    Dinner = pd.read_csv('Diet-Plans/'+planFileName+'/Dinner.csv')
    Total = pd.read_csv('Diet-Plans/'+planFileName+'/Total.csv')

    #Rest Function which creates data
    plan = {}
    for i in range(30):
       plan[i] = 
            'Day'+str(int(Total['Day'].loc[i])):{
                'Breakfast':{
                'Quantity_Item1': str(Breakfast['Quantity Item1'].loc[i]),
                'Description_Item1': Breakfast['Description Item1'].loc[i],
                'Quantity_Item2': str(Breakfast['Quantity Item2'].loc[i]),
                'Description_Item1': Breakfast['Description Item1'].loc[i],
                'Calories': int(Breakfast['Calories'].loc[i]),
                },
                'Snack1':{
                'Quantity_Item1': str(Snack1['Quantity Item1'].loc[i]),
                'Description_Item1': Snack1['Description Item1'].loc[i],
                'Quantity_Item2': str(Snack1['Quantity Item2'].loc[i]),
                'Description_Item1': Snack1['Description Item1'].loc[i],
                'Calories': int(Snack1['Calories'].loc[i]),
                },
                'Lunch':{
                'Quantity_Item1': str(Lunch['Quantity Item1'].loc[i]),
                'Description_Item1': Lunch['Description Item1'].loc[i],
                'Quantity_Item2': str(Lunch['Quantity Item2'].loc[i]),
                'Description_Item1': Lunch['Description Item1'].loc[i],
                'Calories': int(Lunch['Calories'].loc[i]),
                },
                'Snack2':{
                'Quantity_Item1': str(Snack2['Quantity Item1'].loc[i]),
                'Description_Item1': Snack2['Description Item1'].loc[i],
                'Quantity_Item2': str(Snack2['Quantity Item2'].loc[i]),
                'Description_Item1': Snack2['Description Item1'].loc[i],
                'Calories': int(Snack2['Calories'].loc[i]),
                },
                'Dinner':{
                'Quantity_Item1': str(Dinner['Quantity Item1'].loc[i]),
                'Description_Item1': Dinner['Description Item1'].loc[i],
                'Quantity_Item2': str(Dinner['Quantity Item2'].loc[i]),
                'Description_Item1': Dinner['Description Item1'].loc[i],
                'Calories': int(Dinner['Calories'].loc[i]),
                },
                'Total':{
                'Calories_Consume': int(Total['Total Day Calories'].loc[i]),
                'Calories_Burn': int(Total['Calories Burn'].loc[i]),
                },
        },
    #print(plans)
    return plan

def get_fullplan(planFileName):
    Plan = pd.read_csv('Diet-Plans/'+planFileName+'/Bulking Plan.csv')
    Total = pd.read_csv('Diet-Plans/'+planFileName+'/Total.csv')
    return {
    'name': Plan['Plan Name'].loc[0],
    'total_plan_calories_consume': int(Total['Total Day Calories'].loc[30]),
    'total_plan_calories_burn': int(Total['Calories Burn'].loc[30]),
    'days': get_plan(planFileName)
    }
