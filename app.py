from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "secret_key"

@app.route("/")
def index():
    if "number_to_guess" not in session:
        session["number_to_guess"] = random.randint(1, 100)
    return render_template("index.html")

@app.route("/guess", methods=["POST"])
def guess():
    number_to_guess = session["number_to_guess"]
    guess = int(request.form["guess"])
    tries = int(request.form["tries"]) + 1
    difference = abs(guess - number_to_guess)
    if difference > 25:
        result = "Your guess is too high" if guess > number_to_guess else "Your guess is too low"
        color = "red"
    elif 10 <= difference <= 25:
        result = "Your guess is high" if guess > number_to_guess else "Your guess is low"
        color = "orange"
    elif 5 <= difference <= 10:
        result = "Your guess is slightly high" if guess > number_to_guess else "Your guess is slightly low"
        color = "yellow"
    else:
        result = f"Congratulations! You guessed the number in {tries} tries."
        color = "green"
        return render_template("win.html", result=result, color=color)
    return render_template("result.html", result=result, color=color, tries=tries)

@app.route("/play_again", methods=["POST"])
def play_again():
    session["number_to_guess"] = random.randint(1, 100)
    session["tries"] = 1
    return render_template("index.html")

if __name__ == "__main__":
    app.run()