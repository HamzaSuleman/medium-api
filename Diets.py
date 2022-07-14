import pandas as pd

def get_plan(planFileName):
    #Calling Data From excel
    Breakfast = pd.read_excel(planFileName,'Breakfast')
    Snack1 = pd.read_excel(planFileName,'Snack#1')
    Lunch = pd.read_excel(planFileName,'Lunch')
    Snack2 = pd.read_excel(planFileName,'Snack#2')
    Dinner = pd.read_excel(planFileName,'Dinner')
    Total = pd.read_excel(planFileName,'Total')

    #Rest Function which creates data
    plan = []
    for i in range(30):
       plan.append({
            int(Total['Day'].loc[i]):{
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
        },})
    #print(plans)
    return plan

def get_fullplan(planFileName):
    Plan = pd.read_excel(planFileName)
    Total = pd.read_excel(planFileName,'Total')
    return {
    'name': Plan['Plan Name'].loc[0],
    'total_plan_calories_consume': int(Total['Total Day Calories'].loc[30]),
    'total_plan_calories_burn': int(Total['Calories Burn'].loc[30]),
    'days': get_plan(planFileName)
    }