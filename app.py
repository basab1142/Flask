from flask import Flask, render_template
from flask.json import jsonify

app = Flask(__name__)


MODELS = [{
  "id": 1,
  "title" : "Caption-generator",
  "built-by" : "basab_g"
},
{
  "id": 2,
  "title" : "Dog-classification",
  "built-by" : "nyash"
},
{
  "id": 3,
  "title" : "Indian-Car-Plate",
  "built-by" : "nyash"
}          
  ]

@app.route("/")
def hello_world():
  return render_template("home.html", MODELS=MODELS)

@app.route("/api/models")
def Model_view():
  return jsonify(MODELS)
  


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
