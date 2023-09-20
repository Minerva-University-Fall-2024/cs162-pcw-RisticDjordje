# Flask FAQ

This README provides answers to common questions about Flask, a microframework for Python.

## What is Flask and why is it considered as a microframework?

Flask is a lightweight web framework for Python. It is considered a microframework because it provides only the essentials for building web applications, allowing developers to add components as needed. This minimalist approach gives developers more flexibility and control over their application's structure.

## Roles of Parts in a Flask App

- **templates**: Templates in Flask are used for rendering dynamic HTML content.
- **static files**: Static files, such as CSS, JavaScript, and images, are served by Flask without any processing.
- **requirements.txt**: This file lists the Python packages and their versions required for the project.
- **virtual environment (venv)**: A virtual environment isolates project dependencies, ensuring they don't interfere with system-wide packages.
- **render_template**: This function is used to render HTML templates in Flask.
- **redirect**: The `redirect` function is used to redirect users to a different URL.
- **url_for**: The `url_for` function generates URLs for routes in Flask.
- **session**: The `session` object is used for storing user-specific data between requests.

## Common Flask Commands

- `$ pip3 install -r requirements.txt`: Installs project dependencies from the `requirements.txt` file.
- `$ export FLASK_APP=app`: Sets the entry point for the Flask app.
- `$ python3 -m flask run`: Starts the Flask development server.

## Running a Flask App

There are two common ways to run a Flask app:

1. `export FLASK_APP=app.py` followed by `python3 -m flask run`
   - This method sets the entry point to `app.py` and runs the Flask app.
   
2. `python3 app.py`
   - This directly runs the `app.py` script as the Flask app.

Use the first method when you want to set the entry point dynamically, and use the second method when you want a simpler, direct execution.

## Defining Versions in requirements.txt

Defining specific versions of libraries in `requirements.txt` ensures that your project uses compatible dependencies. You can find the recommended versions for libraries by checking the library's documentation or using `pip freeze` to see the currently installed versions.

## @app.route Decorator

The `@app.route` decorator is used to define URL routes in Flask. It associates a function with a specific URL and HTTP methods. Placing it before a function definition tells Flask which URL should trigger that function. By default, the `methods` parameter is set to `['GET']`, meaning the route only responds to HTTP GET requests.

```python
@app.route('/', methods=['GET'])
def main():
    return 'Hello'
```
By default, the methods parameter is set to ['GET'], meaning the route only responds to HTTP GET requests.

### Decorators in Flask
A decorator is a function that modifies the behavior of another function. In Flask, decorators are used to add functionality to routes or functions, such as authentication, authorization, or request preprocessing. They help keep code organized and make it easier to apply common functionality to multiple routes.

### config Attribute in Flask
The config attribute in a Flask app holds configuration settings. You can define custom configuration values by creating a config.py file and loading it into your app using app.config.from_object('config'). For example, you can set TESTING=True or SECRET_KEY='abc' in the config.py file.

### JSON in Web Servers
JSON (JavaScript Object Notation) is a lightweight data interchange format. Modern servers often return data in JSON format because it is easy to parse and widely supported by web applications. It allows structured data to be sent between the server and client.

### Default Host and Port in Flask
The default host and port for Flask are 127.0.0.1 (localhost) and 5000, respectively. You can change these settings when running the app using the --host and --port options with the flask run command. For example:

```$ flask run --host=0.0.0.0 --port=8080
```

This would run the app on all available network interfaces and port 8080.