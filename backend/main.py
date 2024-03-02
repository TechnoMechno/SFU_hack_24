from flask import Flask, render_template, request, jsonify
import requests
app = Flask(__name__)

sessions = []
URL = "https://random-data-api.com/api/v3/projects/05db0f7a-fe9e-49d0-b8ec-80fa835faa2b?api_key=4yjwvUY_YAaP1_iGoEMJrg"


@app.route("/", methods=["GET"])
def hello():
    return "Hmmm! You shouldn't be here! Try to go somewhere else...."


# @app.route("/add/<session-id>")
# def add_user():
#     return session.push(sess)

@app.route("/get-message")
def get_message():
    r = requests.get(URL)
    print(r.json)
    return r.json()


if __name__ == "__main__":
  app.run(debug=True)

# function getMockMessage() {
#     const url = 'http://localhost:5000/get-message'
#     const response = fetch(url)
#     console.log(response);
#     document.getElementById("<id>").innerHTML = response;
# }

# ./backend/.venv/Scripts/activate
# python3 main.py
# To close -> deactivate