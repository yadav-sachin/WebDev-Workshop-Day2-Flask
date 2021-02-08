## Common FAQ:
**1. Why do we need to pass "__ name __" to the Flask Class when creating a flask application, when __ name __ is always = __ main __ when we execute the code from terminal.
- ```app = Flask(__name__)```
- There are many ways to run a flask application. One of them is ```flask run``` command in terminal. In this case if we would have writtern the ```Flask("__main__")```, the flask library which may be running from other directory would not be able to know the location of static, templates folders and other files in our flask application.
- That's why we put app.run under the if clause, so that if we import app variable in another program, the app.run statement is not executed.
  
**2.  Where did we define reviews table in our database?**
```py
class Review(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    genre = db.Column(db.String(100))
    rating  = db.Column(db.Integer, nullable = False)
    created_at = db.Column(db.DateTime, default = datetime.now)
```
- Here we use an ORM (object relational mapping) framework named SQLAlchemy.
- So when we defined the Class Review in our program and run the statement ```db.create_all()```.
- Under the hood, it "maps" our classes and objects derived from db.model in Python program to actual tables and rows in an SQL database.
- So the above class declaration is equivalent to executing the below SQL command:
```SQL
CREATE TABLE reviews(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    genre VARCHAR(100),
    rating INTEGER NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

**3. Why we use ORM like SQLAlchemy? Can we write SQL queries instead in our Flask Application?**
- ORM gives an object oriented abstraction to the operations performed using SQL queries.
- That gives benefit for us to be able to write less code and more readable.

For example:
```py
    to_deleted = Review.query.filter_by(id = review_id).one()
    db.session.delete(to_deleted)
```
is equivalent to SQL command:
```sql
DELETE from reviews
WHERE id = <put_review_id_here>;
```

We can execute SQL queries in Flask using ```db.execute(<SQL_QUERY>)```.
For example,replace ```to_deleted = Review.query.filter_by(id = review_id).one(); db.session.delete(to_deleted)```
```py
db.execute("DELETE from reviews WHERE id = {};".format(review_id));
```
- One more benefit of using ORM is it super easy to switch from one SQL database to another. In app, we use an SQLite Database. For migrating to an mySQL or PostgresSQL database, all we need to change is the ``app.config['SQLALCHEMY_DATABASE_URI']``` URI for the database.

### Try it Yourself
```py
print(Review.query)
```
- In the terminal, you would see that under the hood, Review.query is actually an SQL query under the hood.

**4. Why we used one() here, when we know only one row will have that id (as its primary key)**
By default, the query in <Class_Name>.query.all() returns a list. But instead of a list, we wanted a single object.
Other way of doing the same can be using list indices in python.
Like
```py
review_list = Review.query.filter_by(id = reviewID).all()
wanted_review = review_list[0]
```

**5. Why in the server, we need to check that the rating submitted via the form for it to be less than or equal to 5, even though we only gave options from 1 to 5 in HTML**
- A rule of thumb in server-side programming is to never trust the inputs from the user.
- A malicious user can easily manipulate the HTML files (as shown in workshop using Chrome Dev Tools) or overcome any client-side javascript checking (by disabling Javascript in Browser).
- SO it is very necessary to verify the input once, before adding it to the Database.

**6. Why in the default value of DateTime, we passed a function**
```py
created_at = db.Column(db.DateTime, default = datetime.now)
```
In the default parameter in SQLAlchemy, we pass a python function. datetime.now is a function in Python which returns the current datetime.
In case the created_at time in not given by user, the SQLALchemy will call the function datetime.now, and set the value to the return value of the function.

**7. Why the html page was not able to access files outside src folder. But when opened the html page directly from file explorer, it was able to load the image**
- When the HTML file was rendered by the Flask server, it requested for a resource outside the static folder on the server. Any request by the HTML file to fetch resources outside the static folder on server was simply denied by the server.
- But when we opened the HTML file directly from Browser, there was no server involved, that's why it was able to access any files outside the static folder.
