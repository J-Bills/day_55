from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#Creating pre-specified data types for our paths
@app.route("/<path:username>/<name>/<int:number>")
def greetings(name, number, username):
    return f"hello {name}! you are the {number} years old! \n {username}"

# def delay_decorator(function):
#     def wrapped():
#         #do something before
#         time.sleep(2)
#         function()
#         time.sleep(5)
#         #do something after
#     return wrapped

# @delay_decorator
# def say_hello():
#     print('hello')
    
# def say_bye():
#     print('bye')


if __name__ == "__main__":
    app.run(debug=True)
    # say_hello()
    # say_bye()
    