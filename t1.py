from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route("/")
def home():
    return"<h1>Hello<h1>THis is home page"

@app.route("/<name>")
def user(name):
    return f"hello {name}"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__=="__main__":
    app.run()