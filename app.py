from flask import Flask,jsonify, request

app = Flask(__name__)
print(__name__)

#Normal strings in Python are stored internally as 8-bit ASCII, 
# while Unicode strings are stored as 16-bit Unicode. 
# This allows for a more varied set of characters, 
# including special characters from most languages in the world.
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    #add task
]


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

#tasks[-1]: returns the last task. In python, positions can be referred with 
#index 0,1,2.. or -1,-2,-3..(reverse)

    #Code Here
    

#Code for GET Api


if (__name__ == "__main__"):
    app.run(debug=True)