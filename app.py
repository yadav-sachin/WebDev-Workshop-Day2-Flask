from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/editReview")
def edit():
    return render_template("edit_review.html")

@app.route("/addReview")
def add():
    return render_template("add_review.html")

if __name__ == "__main__":
    app.run(debug = True)
