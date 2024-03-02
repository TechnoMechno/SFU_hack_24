# from APIManager import 
from flask import Flask, after_this_request, jsonify, render_template, request

app = Flask(__name__)

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
    r = initialize()
    print(r.json)
    return r.json()


if __name__ == "__main__":
  app.run(debug=True)

# ./backend/.venv/Scripts/activate
# python3 main.py
# To close -> deactivate