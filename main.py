from flask import Flask, render_template, request
from datetime import datetime as dt
import pandas

x = dt.now()

data = pandas.read_csv("9_Provinces.csv")

list_of_provinces = []
for province in data.province:
    list_of_provinces.append(province)

correct_guesses = 0
number_of_correct_guesses = f"{correct_guesses}/{len(list_of_provinces)} Provinces Correct"
guessed_provinces = []

app = Flask(__name__)


@app.route("/")
def home():
    # Footer #
    year = x.year
    return render_template("index.html", num_guesses=correct_guesses, year=year)


@app.route("/", methods=["POST"])
def receive_data():
    global number_of_correct_guesses, correct_guesses
    year = x.year
    user_province = request.form["province"]
    while correct_guesses < len(list_of_provinces):
        if user_province in list_of_provinces:
            if user_province not in guessed_provinces:
                correct_guesses += 1
                guessed_provinces.append(user_province)
                return render_template("index.html", list_guesses=guessed_provinces,
                                       num_guesses=correct_guesses)
            else:
                old_guess = f"You've already guessed {user_province}"
                return render_template("index.html", list_guesses=guessed_provinces,
                                       num_guesses=correct_guesses, year=year, old_guess=old_guess)
        else:
            return render_template("index.html", list_guesses=guessed_provinces,
                                   num_guesses=correct_guesses, year=year)

    return render_template("index.html", list_guesses=guessed_provinces,
                           num_guesses=correct_guesses, year=year)


if __name__ == "__main__":
    app.run(debug=True)
