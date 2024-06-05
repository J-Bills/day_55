from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# def delay_decorator(function):
#     def wrapped():
#         #do something before
#         time.sleep(2)
#         function()
#         time.sleep(5)
#         #do something after
#     return wrapped

@delay_decorator
def say_hello():
    print('hello')
    
def say_bye():
    print('bye')


if __name__ == "__main__":
    app.run()
    say_hello()
    say_bye()