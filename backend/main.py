from flask import Flask, render_template, redirect, after_this_request, request
from API_Manager import process, initialize, user_to_gpt, get_GPT_unformat_output, get_GPT_content
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app, resources={r"/get-message": {"origins": "*"}})

@app.route("/", methods=["GET"])
def actualFirst():
  return render_template("actualFirstPage.html")

# @app.route("/add/<session-id>")
#     return session.push(sess)

@app.route("/init")
def firstPage():
  return render_template("firstPage.html")

@app.route("/game")
def gamePage():
  return render_template("gamePage.html")

@app.route("/last")
def lastPage():
  return redirect("/")

@app.route("/get-message", methods=["GET"])
def get_message():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    
    # Assuming get_GPT_content returns a JSON string
    r = initialize()
    print(r)
    
    # You can directly return JSON data using jsonify in Flask
    return r


@app.route("/process-input/<input>", methods=["GET"])
def process_input(input):
    print(input)
    r = process(input)
    print(r)
    return r


if __name__ == "__main__":
  app.run(debug=True)

# ./backend/.venv/Scripts/activate
# python3 main.py
# To close -> deactivate