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
    return render_template("index.html", reviews = all_reviews)

@app.route("/editReview/<int:reviewID>", methods = ["GET", "POST"])
def edit(reviewID):
    if request.method == "POST":
        #logic for editing the row in teh database
        try:
            to_edited = Review.query.filter_by(id = reviewID).one()
            to_edited.name = request.form['movie_name']
            to_edited.genre = request.form['genre']
            to_edited.rating = request.form['rating']
            db.session.commit()
            return redirect("/")
        finally:
            return redirect("/")
    else: 
        wanted_review = Review.query.filter_by(id = reviewID).one()
        return render_template("edit_review.html", review = wanted_review)

@app.route("/addReview/", methods = ["GET", "POST"])
def add():
    if request.method == "POST":
        if not verify_input(request.form):
            return redirect("/")
        new_review = Review(name = request.form['movie_name'], genre = request.form['genre'], rating = request.form['rating'])
        db.session.add(new_review)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("add_review.html")

@app.route("/deleteReview/<int:review_id>")
def delet(review_id):
    to_deleted = Review.query.filter_by(id = review_id).one()
    db.session.delete(to_deleted)
    db.session.commit()
    return redirect("/")

def verify_input(obj):
    if obj["rating"] > 5: 
        return False


if __name__ == "__main__":
    app.run(debug = True)
