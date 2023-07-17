
# import Flask module from flask package
from flask import Flask

#Flask create instances of web application
app = Flask(__name__)

# define the routes, the ececuted code will be access localhost:5000
@app.route("/")

# This line define function that will be executed if we access route
def hello():
    return "Hello World!"


if __name__ == '__main__':
    # debug = True will print out possible python errors on the web page helping us traces the errors
    app.run(debug=True)