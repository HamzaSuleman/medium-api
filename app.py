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
  },
   {
    "Size": "XL",
    "Toppings":"Cheese",
    "Crust":"Thin Crust",
  },
   {
    "Size": "Large",
    "Toppings":"Mushrooms",
    "Crust":"Pan Crust",
  },
   {
    "Size": "Small",
    "Toppings":"pork",
    "Crust":"Thin Crust",
  },
   {
    "Size": "XXL",
    "Toppings":"Chicken",
    "Crust":"Kabab Crust",
  },
   {
    "Size": "Small",
    "Toppings":"Cheese",
    "Crust":"Thin Crust",
  },
   {
    "Size": "Small",
    "Toppings":"Cheese",
    "Crust":"Thin Crust",
  },
   {
    "Size": "Small",
    "Toppings":"Cheese",
    "Crust":"Thin Crust",
  },
   {
    "Size": "Small",
    "Toppings":"Cheese",
    "Crust":"Thin Crust",
  },
    {
    "Size": "Large",
    "Toppings":"Cheese",
    "Crust":"Stuffed Crust",
  },
   {
    "Size": "XL",
    "Toppings":"Cheese",
    "Crust":"Thin Crust",
  },
   {
    "Size": "Large",
    "Toppings":"Mushrooms",
    "Crust":"Pan Crust",
  },
   {
    "Size": "Small",
    "Toppings":"pork",
    "Crust":"Thin Crust",
  },
]

@app.route('/')
def get():
    response = make_response(jsonify(orders), 200)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__ == '__main__':
    app.run() 
