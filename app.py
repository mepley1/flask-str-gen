from flask import Flask, request, redirect, render_template
from os import urandom
import random
import string

app = Flask(__name__)
app.config["SECRET_KEY"] = str(urandom(24));

@app.route('/')
def index():
    return render_template("index.html", length = 32)

@app.route('/generate', methods = ["POST"])
def greeting():
    POST_num_of_chars = request.form["name"]
    
    pwd = ""
    count = 0
    length = int(POST_num_of_chars)

    while count != length:

        upper = [random.choice(string.ascii_uppercase)]
        lower = [random.choice(string.ascii_lowercase)]
        num = [random.choice(string.digits)]
        symbol = [random.choice(string.punctuation)]
        everything = upper + lower + num + symbol

        pwd += random.choice(everything)
        count += 1
        continue

    if count == length:
        return render_template("index.html", name = pwd, length = length)

if __name__ == '__main__':
    app.run(debug = True)
