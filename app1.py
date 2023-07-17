# import packages
from flask import Flask

# create app
app = Flask(__name__)

# develop api
@app.route("/")
def hello():
    return "I am happy to say hello"

# develop api
@app.route("/mukund")
def greet():
    return "ok"

# develop api
@app.route("/ishita")
def welcome():
    return "I am happy to say hello"

# develop api
@app.route('/hari')
def namaskar():
    return 'Welcome Hari ji, what is your order'

# develop api
@app.route('/ritika')
def namaste():
    return 'Welcome Hari ji, what is your order'

#develop api
@app.route('/<name>')
def good_morning(name):
    return 'Welcome ' +  name +', you are new, what is your order'

# run app
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=False)