<<<<<<< HEAD
# from APIManager import 
from flask import Flask, after_this_request, jsonify, render_template, request
=======
from flask import Flask, render_template, request, jsonify, after_this_request
from API_Manager import process, initialize
>>>>>>> 051fcd433a7990e42f96db43ad23d8c4150fd200

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
<<<<<<< HEAD
    return render_template("frontend/gamePage.html")
=======
    return render_template("../frontend/gamePage.html")
>>>>>>> 051fcd433a7990e42f96db43ad23d8c4150fd200


# @app.route("/add/<session-id>")
# def add_user():
#     return session.push(sess)

@app.route("/get-message")
def get_message():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    r = initialize()
    print(r.json)
    return r.json()


if __name__ == "__main__":
  app.run(debug=True)

# ./backend/.venv/Scripts/activate
# python3 main.py
# To close -> deactivate