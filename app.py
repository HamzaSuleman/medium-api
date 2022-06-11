from flask import Flask, jsonify, make_response

app = Flask(__name__)

orders = {
  "order1": {
    "Size": "Small",
    "Toppings":"Cheese",
    "Crust":"Thin Crust",
  },
  "order2": {
    "Size": "Large",
    "Toppings":"Cheese",
    "Crust":"Stuffed Crust",
  }
}

@app.route('/')
def get():
    response = make_response(jsonify(orders), 200)
    return response

@app.route('/<orderid>')
def get_order(orderid):
  if orderid in orders:
    response = make_response(jsonify(orders[orderid]), 200)
    return response
  else:
    return 'No such data exists'

@app.route('/<orderid>/<items>')
def get_order_item(orderid, items):
  item = orders[orderid].get(items)
  if item:
    response = make_response(jsonify(item), 200)
    return response
  else:
    return 'No such data exists'

if __name__ == '__main__':
    app.run() 
