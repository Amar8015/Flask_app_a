from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/helloworld1")
def hello_world1():
    return "<h1>Hello, World1!</h1>"

@app.route("/helloworld2")
def hello_world2():
    return "<h1>Hello, World2!</h1>"


@app.route("/test")
def test():
    data = request.args.get('x')
    return "this is data from my url {}".format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")
