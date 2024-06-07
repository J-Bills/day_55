from flask import Flask
from random import randint

app = Flask(__name__)

def high():
    return '<h1 style="color:red">Too High, Try Again</h1>' \
            '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
def low():
    return  '<h1 style="color:red">Too low, Try Again</h1>' \
            '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
def correct():
    return  '<h1 style="color:red">You got it!</h1>' \
            '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'

@app.route("/")
def main():
    return "<h1 style='text-align:center'>Guess a number between 0 and 9</h1>" \
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif''>"
            
            
@app.route("/<int:number>")            
def num_route(number):
    if number not in range(0,10):
        return "<h1>Number must be between 0 and 9</h1>"
    elif RANDOM_NUMBER == number:
        result =correct()
    elif RANDOM_NUMBER > number:
        result = low()
    elif RANDOM_NUMBER < number:
        result = high()
    return result



if __name__ == "__main__":
    RANDOM_NUMBER = randint(0,9)
    app.run(debug=True)