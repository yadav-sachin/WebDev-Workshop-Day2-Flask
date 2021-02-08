# Resources and Hints for Tasks:

## Task 1:
**Deploy the Flask application on [Heroku](https://www.heroku.com/).**
- https://flask.palletsprojects.com/en/1.1.x/deploying/
- Or can refer to some tutorials on Youtube for deploying Flask on Heroku.

## Task 2:
**2. In Database, for movies, we stored id, name, rating and creation time. Now add another attribute of "body", which is a text attribute for the movie review. Make changes to the Edit-Add page accordingly. Also reflect the body data in the "index.html" templates.**


## Task 3:
**3. Add Buttons on the Home page for the user to sort the Movie Reviews by Names, Genre, Date Created or Movie Ratings.**
- For example, the sort by rating button will make a GET request to URL "/?sort=rating".
- In the function for "/" URL.
- Fetch the request args for sort key in the dictionary.
- Using if-else clause that what is the value of sort, fetch the rows in some order.
- Just like in SQLAlchemy we had "filter_by" for filtering via some parameter, we also have "order_by" for sorting.
- Similarly write logic for "/?sort=name" and others.

## Task 4.
- **In our application, when the movie was added/edited successfully or there was a failure, we didn't show [alert messages](https://getbootstrap.com/docs/4.0/components/alerts/) to user for success or failure. Add these alerts to the application.**
- https://getbootstrap.com/docs/4.0/components/alerts/
- https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/
- Pass the message to the template as well while rendering.

## Task 5.
**While adding a Movie Review, the user should be able to upload a thumbnail image for the movie. The thumbnail images of the movies will be listed along with their details on the homepage.**
- In the form, add a input of type file.
- https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/
    

Feel free, to ping some admin on Discord channel, if stuck somewhere.