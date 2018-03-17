from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "PUPPIES"


# Make an app.route() decorator here for when the client sends the URI "/puppies"
@app.route("/puppies")
def puppiesFunction():
    return "Yes, puppies!"
@app.route("/puppies/<int:id>")
def puppiesFunctionId(id):
    return "El puppy! %s"  %id


if __name__ == '__main__':
    app.run(debug=True)
