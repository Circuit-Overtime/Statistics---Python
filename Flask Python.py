from flask import Flask,jsonify, request

app = Flask(__name__)

List = [
    {
        'id': 1,
        'Name': u'Sample1',
        'Contact': u'sample1@gmail.com', 
         'Marks' : u'100',
        'done': False
    },
    {
        'id': 2,
        'Name': u'Sample2',
        'Contact': u'sample2@gmail.com', 
        'Marks' : u'98',
        'done': True
    }
]

@app.route("/")
def hello_world():
    return "Welcome to Page!" #success notif

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Provide suitable data" #data missing error
        },400)

    contact = {
        'id': tasks[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    List.append(contact)
    return jsonify({
        "status":"success",
        "message": "Contact added succesfully!" #data add message
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : List
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)