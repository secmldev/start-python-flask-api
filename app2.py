# import packages
from flask import Flask

# create app
myapp = Flask(__name__)

# develop api
@myapp.route("/")
def hello():
    return "I am happy to say hello"

# develop api
@myapp.route("/mukund")
def greet():
    return "ok"

# develop api
@myapp.route("/ishita")
def welcome():
    return "I am happy to say hello"

# develop api
@myapp.route("/<name>")
def namaste(name):
    return "hello, sir " + name

# develop api
@myapp.route("/<name>/<city>")
def my_client(name, city):
    return "hello, sir " + name + "when did you come from " + city


# run app
if __name__ == "__main__":
    myapp.run(host="127.0.0.1", port=8082, debug=False)