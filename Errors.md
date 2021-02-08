##
**1. When submitting the form on editReview, the form was taking us to /editReview/editReview/ instead of /editReview?**
- As discussed in the workshop, we solved it.
- Actually in the form submission of edit_review.html, the action was earlier set to.
```html
action="editReview/{{review.id}}">
```
- Here notice the path does not have a "/" in the beginning.
- If the "/" is missing in the beginning of URL path, it takes us relative to the current path, hence taking us to "/editReview/editReview/"
- We resolved it by putting a "/" in front of the URL, which signifies that this path is relative to the home path instead and not the current path.
```html
action="/editReview/{{review.id}}">
```

**2. In the beginning of the workshop. Why the pre-built app, that I made earlier was not running in the start**.
- Actually there are multiple ways to run Flask application.
- During development phase of that app, I was using ```flask run``` command to run the server it in the Windows system, instead of ```python app.py```.
- But to continuosly update the code on github from terminal, I switched to WSL: Ubuntu during the workshop instead. And in WSL:Ubuntu, some of the libraries were not installed prior to it. And as I was running from flask command, I didn't add the app.run statment in the app.py, due to which the file didn't run.
- As during the workshop, some of you might not have flask in the PATH variables, so the ```flask run``` command would not work, that's why we were using app.run to run the Flask app.
- We resolved this error by putting the code in the app.py
```py
if __name__ == "__main__":
    app.run(debug = True)
```

**3. There was some depreciation warning from the SQLAlchemy library about a feature to monitor changes in development?**
- Just follow the path of init file as given in the warning and set the parameter to False.
