# from APIManager import 
import requests
from flask import Flask, after_this_request, jsonify, render_template, request

app = Flask(__name__)

sessions = []
URL = "https://random-data-api.com/api/v3/projects/05db0f7a-fe9e-49d0-b8ec-80fa835faa2b?api_key=4yjwvUY_YAaP1_iGoEMJrg"


@app.route("/", methods=["GET"])
def hello():
    return render_template("frontend/gamePage.html")


# @app.route("/add/<session-id>")
# def add_user():
#     return session.push(sess)

@app.route("/get-message")
def get_message():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    r = requests.get(URL)
    print(r.json)
    return r.json()


if __name__ == "__main__":
  app.run(debug=True)

# function getHello() {
#     const url = 'http://localhost:5000/get-message'
#     fetch(url)
#     .then(response => response.json())  
#     .then(json => {
#         console.log(json);
#         document.getElementById("demo").innerHTML = JSON.stringify(json)
#     })
# }

# ./backend/.venv/Scripts/activate
# python3 main.py
# To close -> deactivate