
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import itertools
import warnings
warnings.filterwarnings('ignore')


thousand_cal_in_grams = 129.59782

def get_ActiveDiet_Chart(Diets, activeDietName):
    for diet in Diets:
        Plan = pd.read_csv('/Diet-Plans/'+diet+'/'+diet+'.csv')
        if(Plan['Plan Name'].loc[0] == activeDietName):
            return diet

type = ['Weight_Loss_80kg','Bulking_Plan','Weight_Loss_65kg','Weight_Loss_Diabetes']


weights = [80.084757,
80.173661,
80.23,
80.341101,
80.4,
80.45,
80.647513,
80.627513,
80.742
]

weights1 = [79.919649,
79.824525,
79.733806,
79.680023,
79.608485,
79.58,
79.55,
79.37,

]


def TimeSeriesAlgorithm(startDietWeight, currentDay, currentDiet, weightsTillNow):
    
    #calculating weight change
    currentDiet['remaining_cal'] = currentDiet['Total Day Calories'] - currentDiet['Calories Burn'] 
    currentDiet['weight_change'] = ((currentDiet['remaining_cal']/1000) * thousand_cal_in_grams)/1000

    #parsing date as index
    df =  pd.read_csv('dates.csv', parse_dates=['Date'], index_col=['Date'])

    # calculating gain each day
    for i in range(len(df['gain'])):
        if(i == 0):
            df['gain'].iloc[i] = startDietWeight + currentDiet['weight_change'].iloc[i]
        if(i > 0 and i < 30):
            df['gain'].iloc[i] = df['gain'].iloc[i-1] + currentDiet['weight_change'].iloc[i] 

    #Actual Data Should be as below
    ts = df['gain'].resample('D').sum()
    ts = ts[:30]

    # here recieve data from data base of user weight till date now
    for i in range(len(weightsTillNow)):
        df['user_weight'].iloc[i] = weightsTillNow[i]

    # user data recieve from app
    ts_user = df['user_weight'].resample('D').sum()
    ts_user = ts_user[:currentDay-1]

    # find order or arima model
    p=d=q = range(0,3)
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
        except:
            continue

    print('Order: ',orderArima)
    print('AIC: ',minimum_aic)

    # training model with user all weights till now
    ts_f = ts_user
    final_model = ARIMA(ts_f, order=orderArima).fit()

    # predicting weight from range start to end
    prediction = final_model.predict(len(ts_f)-1, len(ts)-1)
    #print(ts_f)
    predictedWeights = []
    actualWeights = []
    for i in range(len(prediction)):
        predictedWeights.append(round(prediction.iloc[i],2))
    for i in range(len(ts)):
        actualWeights.append(round(ts.iloc[i],2))

    return {
            'weights': weightsTillNow,
            'predicted Weights': predictedWeights,
            'Actual Weights': actualWeights,
            }
    


#TimeSeriesAlgorithm(80, 9, 'Paklife Bulking', weights)
