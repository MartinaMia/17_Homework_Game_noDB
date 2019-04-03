from flask import Flask, render_template, request, make_response

app = Flask(__name__)

import datetime             # import of Software
import random


@app.route("/", methods=["GET"])         # Controller
def index():
    secret_number = request.cookies.get("secret_number")  # 1. check if there is already a cookie called secret_number

    current_time = datetime.datetime.now()  # Softwarepackage.class.method

    response = make_response(render_template("index.html", current_time=current_time))  # Jinja Variable))

    if not secret_number:  # 2. if not, create a new cookie
        new_secret = random.randint(1, 30)
        response.set_cookie("secret_number", str(new_secret))
    return response

@app.route("/result", methods=["POST"])
def result():
    guess = int(request.form.get("guess"))
    secret_number = int(request.cookies.get("secret_number"))

    while True:
        if guess == secret_number:
            message = "You've guessed it - congratulations! It's number " + str(secret_number)
            response = make_response(render_template("result.html", message=message))
            response.set_cookie("secret_number", str(random.randint(1, 30)))        # set the new secret number
            return response

        elif guess > secret_number:
            message = "Your guess is not correct... try something smaller"
            return render_template("result.html", message=message)

        elif guess < secret_number:
            message = "Your guess is not correct... try something bigger"
            return render_template("result.html", message=message)

if __name__ == '__main__':
    app.run(debug=False)

