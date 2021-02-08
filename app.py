from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# Create a Flask application object, and store that in a variable named "app", by convention the name of this variable is set to app.
app = Flask(__name__)
# Set the path for the SQLALchemy Database
# In case of mySQL, we need to provide username, password and server of the database as well in the URI
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
#Create a SQLALchemy engine object for the database
db = SQLAlchemy(app)

# Create a Class Review, it is mapped to a table definition named "reviews" by the SQLAlchemy engine
class Review(db.Model):
    # Primary key for the Table, as two movies can have same name
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    genre = db.Column(db.String(100))
    rating = db.Column(db.Integer, nullable = False)
    #the time of creation, if not provided by user, set it to the current time
    created_at = db.Column(db.DateTime, default = datetime.now)

# Creates tables in the Database, according to the classes derived from db.Model
# This is a bad practice to write this statement here. Ideally you should go to ptyhon terminal, and execute 
# >>> from app import db
# >>> db.create_all()
# Once, so that this statement does not get executed everytime we run the program.
db.create_all()

# If any user requests URL / (via GET Request)
# In browsers, however the "/" at the end of URL is hidden by the browser.
@app.route("/")
def home():
    all_reviews = Review.query.all()
    # Pass the all_reviews list to the template as "reviews"
    return render_template("index.html", reviews = all_reviews)

# If there is a request on URL /addReview/
# Here it handles both POST requests and GET requests
@app.route("/addReview/", methods = ["GET", "POST"])
def addPage():
    if request.method == "GET":
        # In case of GET request, a user just visiting the SITE
        return render_template("add_review.html")
    else:
        #else POST request, where a user has submitted a form to this URL via POST method in the form
        try:
            #first verify that the input is all correct and doesn't have bad values
            if verify_input(request.form):
                # Create an object of class Review with the form data
                new_review = Review(name = request.form['movie_name'], genre = request.form['genre'], rating = request.form['rating'])
                # Here the SQLAlchemy will add the object ( a new row under the hood) in the database
                db.session.add(new_review)
                # commit all changes that we made till now to the database
                db.session.commit()
        finally:
            return redirect("/")

# Manages GET and POST request at /editReview/<expecting an integer here>
# The integer in the PATH, will be passed to the function as an argument
# In case the PATH contains a string, instead of URL, it will not match here and will give 404 Error, as we defined int here
@app.route("/editReview/<int:review_id>", methods = ["GET", "POST"])
def editPage(review_id):
    if request.method == "GET":
        try:
            #Fetch the object with that id
            curr_review = Review.query.filter_by(id = review_id).one()
            # this object will be available in the template with name "review"
            return render_template("edit_review.html", review = curr_review)
        except:
            # in case of any error, take user to home
            return redirect("/")
    else:
        try:
            # When submitting form over POST request
            # Verify the input once
            if verify_input(request.form):
                # Fetch the object
                # Make changes to it
                # commit the new changes to the database
                review_to_edit = Review.query.filter_by(id = review_id).one()
                review_to_edit.name = request.form['movie_name']
                review_to_edit.genre = request.form['genre']
                review_to_edit.rating = request.form['rating']
                db.session.commit()
        finally:
            return redirect("/")


@app.route("/deleteReview/<int:review_id>")
def deletePage(review_id):
    try:
        # Fetch the desired object, pass it to delete function to remove it from databases, finally commit changes to the database
        review_to_delete = Review.query.filter_by(id = review_id).one()
        db.session.delete(review_to_delete)
        db.session.commit()
    finally:
        return redirect("/")

# Check the input
# Return True if everything is fine
# else return False
def verify_input(req_form):
    try:
        if "movie_name" not in req_form:
            return False
        if "rating" not in req_form:
            return False
        if 1 <= int(req_form['rating']) <= 5:
            return True
        else:
            return False
    except:
        return False

# If we are executing the app.py directly from the terminal
if __name__ == "__main__":
    # Run the Flask application in Development mode
    # When using the application in Production, make the debug to False
    app.run(debug = True)
