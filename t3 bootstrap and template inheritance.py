from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("2.1.html")

@app.route("/test")
def test():
    return render_template("2.2 .html")


if __name__=="__main__":
    app.run(debug=True)