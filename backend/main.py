from flask import Flask, render_template, request, jsonify, after_this_request
from API_Manager import process, initialize

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
  return render_template("gamePage.html")
# @app.route("/add/<session-id>")
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