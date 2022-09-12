
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
#from datetime import date
import itertools
import warnings
warnings.filterwarnings('ignore')


def get_ActiveDiet_Chart(Diets, activeDietName):
    for diet in Diets:
        Plan = pd.read_csv('../../Diet-Plans/'+diet+'/'+diet+'.csv')
        if(Plan['Plan Name'].loc[0] == activeDietName):
            return diet

type = ['Weight_Loss_80kg','Bulking_Plan','Weight_Loss_65kg','Weight_Loss_Diabetes']

#activeDietName = 'Weight_Loss_65kg'
thousand_cal_in_grams = 129.59782
activeDietName = get_ActiveDiet_Chart(type,'Paklife Bulking')
currentDiet = pd.read_csv("../../Diet-Plans/"+activeDietName+"/Total.csv")

currentDiet['remaining_cal'] = currentDiet['Total Day Calories'] - currentDiet['Calories Burn'] 
currentDiet['weight_change'] = ((currentDiet['remaining_cal']/1000) * thousand_cal_in_grams)/1000
print(currentDiet)

currentDietWeight = 80
currentDay = 9

df =  pd.read_csv('dates.csv', parse_dates=['Date'], index_col=['Date'])

for i in range(len(df['gain'])):
    if(i == 0):
        df['gain'].iloc[i] = currentDietWeight + currentDiet['weight_change'].iloc[i]
    if(i > 0 and i < 30):
        df['gain'].iloc[i] = df['gain'].iloc[i-1] + currentDiet['weight_change'].iloc[i] 


ts = df['gain'].resample('D').sum()
ts = ts[:30]
print(ts)
# here recieve data from data base of user weight till date now
ts_user = df['user_weight'].resample('D').sum()
ts_user = ts_user[:currentDay-1]
print(ts_user)

#ts_user.iloc[13] = 82
#ts_user.iloc[14] = 80
#print(ts)
#print(ts_user)

p=d=q = range(0,5)
pdq = list(itertools.product(p,d,q))

minimum_aic = 100000
orderArima = (0,0,0)
for parem in pdq:
    try:
        model_arima = ARIMA(ts, order=parem)
        model_arima_fit = model_arima.fit()
        if (model_arima_fit.aic < minimum_aic):
            minimum_aic = model_arima_fit.aic
            orderArima = parem
        #print(parem,model_arima_fit.aic)
    except:
        continue

print('Order: ',orderArima)
print('AIC: ',minimum_aic)

#ts_f = ts[:round(len(ts)*0.8)]
#ts_f = ts_user[:20]
ts_f = ts_user
#print(len(ts_f))
final_model = ARIMA(ts_f, order=orderArima).fit()

prediction = final_model.predict(len(ts_f)-1, len(ts)-1)

ts.plot(legend = True, label = 'Actual', figsize=(10,6))
#print(ts)
ts_f.plot(legend = True, label = 'Trained', figsize=(10,6))
prediction.plot(legend = True, label = 'prediction')
print(prediction)
plt.show()
#final_prediction = pd.concat([ts_f,prediction])
#final_prediction = final_prediction.reset_index()
#final_prediction = final_prediction.drop('index', axis=1)
#print(final_prediction)

