# Resources and Hints for Tasks:

## Task 1:
**Deploy the Flask application on [Heroku](https://www.heroku.com/) or [Python Anywhere](https://www.pythonanywhere.com/)**
- For Deploying, it is elementary to setup a Version Control System first. [Tutorial](https://www.freecodecamp.org/news/a-beginners-guide-to-git-how-to-create-your-first-github-project-c3ff53f56861/#:~:text=%232%20step%20%E2%80%94%20Your%20first%20GitHub%20project!&text=Click%20on%20it!&text=The%20repository%20creation%20page%20will,this%20repository%20with%20a%20README%E2%80%9D.)
- https://flask.palletsprojects.com/en/1.1.x/deploying/
- Or can refer to some tutorials on Youtube for deploying Flask.
- For remote Database, you can use the free-tier version of [JawsDB MySQL](https://elements.heroku.com/addons/jawsdb) add-on on Heroku. It gives 5 MB of data storage for free. You may be required to verify your account using Debit Card details first on Heroku Platform. It would be free, make sure to choose free-tier plan.
- Make sure that the Database URI is accessed from the environment configuration variables [1](https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables) [2](https://devcenter.heroku.com/articles/config-vars).

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