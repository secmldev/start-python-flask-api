# import packages
from flask import Flask

# create app
app = Flask(__name__)

# start api development
@app.route("/")
def hello() -> str:
    return "Hello World"

# develop api
@app.route("/ishita")
def welcome():
    return "Hello Ishita, what is your order"

# develop api
@app.route("/<name>")
def greeting(name):
    return 'Hello,' + name + ' what is your order and where do you want to eat it and how do you want to pay'

# develop api
@app.route("/<name>/<city>")
def my_client(name, city):
    return "hello, sir " + name + "when did you come from " + city

# develop api
@app.route('/sale/<transaction_id>')
def get_sale(transaction_id = 0):
    return 'The trasaction is ' + str(transaction_id)


# develop api
@app.route('/person/<name>/<father>/<mother>/<school>/<section>')
def about_person(name, father, mother, school, section):
    print('Name: ' + name)
    print('Father: ' + father)
    print('Mother: ' + mother)
    print('School: ' + school)
    print('Section: ' + section)
    return ({"name": name, "father": father, "mother": mother, "school": school, "section": section})



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8084, debug=False)