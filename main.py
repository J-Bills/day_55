from flask import Flask
import time

app = Flask(__name__)

#adding html styling to the hello_world() functin using decorators
def make_bold(function):
    def wrapper():
        return f'<b>{function()}</b>'
    return wrapper

def make_emphasis(function):
    def wrapper():
        return f'<em>{function()}</em>'
    return wrapper

def make_underlined(function):
    def wrapper():
        return f'<u>{function()}</u>'
    return wrapper



@app.route("/")
@make_bold
@make_emphasis
@make_underlined
def hello_world():
    return "<p>Hello, World!</p>" \
            # '<img src="https://t3.ftcdn.net/jpg/02/95/44/22/360_F_295442295_OXsXOmLmqBUfZreTnGo9PREuAPSLQhff.jpg">' \
            # '<h1 style="text-align: center">Picture</h1>'

#Creating pre-specified data types for our paths
@app.route("/<path:username>/<name>/<int:number>")
def greetings(name, number, username):
    return '<h1 style=" text-align: center">f"hello {name}! you are the {number} years old! \n {username}"</h1>'

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
    