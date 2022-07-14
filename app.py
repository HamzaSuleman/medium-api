from flask import Flask, jsonify, make_response
import pandas as pd
import json

app = Flask(__name__)

df = pd.read_csv('friends.csv')
framelength = len(df.index)

data = []

for i in range(framelength):
    data.append(
    {
        'name': df['name'].loc[i],
        'marks': str(df['marks'].loc[i]),
        'city': df['city'].loc[i]
    })
#print(data)

@app.route('/')
def get():
    response = make_response(jsonify(data), 200)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__ == '__main__':
    app.run() 
