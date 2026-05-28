from flask import Flask, render_template, request, redirect, session
from datetime import date

app = Flask(__name__)
app.secret_key = "love_secret_key"

PASSWORD = "14.01.2006"

# ❤️ ДАТА НАЧАЛА ОТНОШЕНИЙ (поменяй на свою)
START_DATE = date(2025, 1, 4)


@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        password = request.form.get("password")

        if password == PASSWORD:
            session["access"] = True
            return redirect("/home")

        return render_template("login.html", error="Неверный пароль ❤️")

    return render_template("login.html")


@app.route("/home")
def home():

    if not session.get("access"):
        return redirect("/")

    # 💖 СЧЁТЧИК ДНЕЙ
    today = date.today()
    days_together = (today - START_DATE).days

    return render_template("index.html", days=days_together)


@app.route("/about")
def about():

    if not session.get("access"):
        return redirect("/")

    return render_template("about.html")


@app.route("/forum")
def forum():

    if not session.get("access"):
        return redirect("/")

    return render_template("forum.html")


@app.route("/privet")
def privet():

    if not session.get("access"):
        return redirect("/")

    return render_template("privet.html")


@app.route("/index2")
def index2():

    if not session.get("access"):
        return redirect("/")

    return render_template("index2.html")


if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)