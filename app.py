from flask import Flask, render_template, request, redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
db = SQLAlchemy(app)

review = []

# ORM --> Object Relational Mapping

class Review(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    genre = db.Column(db.String(100))
    rating  = db.Column(db.Integer, nullable = False)
    created_at = db.Column(db.DateTime, default = datetime.now)


db.create_all()

@app.route("/")
def home():
    all_reviews = Review.query.all()
    print(all_reviews)
    return render_template("index.html", reviews = all_reviews)

@app.route("/editReview/")
def edit():
    return render_template("edit_review.html")

@app.route("/addReview/", methods = ["GET", "POST"])
def add():
    if request.method == "POST":
        new_review = Review(name = request.form['movie_name'], genre = request.form['genre'], rating = request.form['rating'])
        db.session.add(new_review)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("add_review.html")

if __name__ == "__main__":
    app.run(debug = True)
