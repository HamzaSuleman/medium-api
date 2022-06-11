from crypt import methods

from flask import Flask, jsonify, make_response

app = Flask(__name__)

data = [
  {
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto",
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "userId": 1
  },
  {
    "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla",
    "id": 2,
    "title": "qui est esse",
    "userId": 1
  }
]

@app.route('/api', methods=['GET'])
def get():
    response = make_response(jsonify(data), 200)
    return response


if __name__ == '__main__':
    app.run() 
