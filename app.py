# save this as app.py
from flask import Flask

from src.flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "DevOps, Atividade somativa1"

if __name__ == "__main__":
    app.run(debug=True)
