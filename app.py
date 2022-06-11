from flask import Flask, jsonify, make_response

app = Flask(__name__)

orders = [
   {
    "Size": "Small",
    "Toppings":"Cheese",
    "Crust":"Thin Crust",
  },
  {
    "Size": "Large",
    "Toppings":"Cheese",
    "Crust":"Stuffed Crust",
  }
]

@app.route('/')
def get():
    response = make_response(jsonify(orders), 200)
    return response

if __name__ == '__main__':
    app.run() 
