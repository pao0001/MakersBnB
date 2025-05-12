# Flask Security and Frontend Libraries Documentation

This document provides a concise overview and links to the official documentation for Flask-Login, Flask-WTF, Flask-Bcrypt, and Bootstrap, commonly used in Flask web development.

_Remember to run pip freeze > requirements.txt if you add any of the following to your project: ```flask-wtf```, ```flask-login```, ```flask-bcrypt``` and/or```peewee``` to update the list of dependencies._

## Flask-Login

* **Description:** Flask-Login provides user session management for Flask. It handles user login, logout, and session persistence.
* **Links:**
    * [Flask-Login Documentation](https://flask-login.readthedocs.io/en/latest/)
    * [Flask-Login on PyPI](https://pypi.org/project/Flask-Login/)
* **Example Implementation:**

    ```python
    from flask import Flask
    from flask_login import LoginManager, UserMixin, login_user

    app = Flask(__name__)
    login_manager = LoginManager()
    login_manager.init_app(app)

    class User(UserMixin):
        def __init__(self, id):
            self.id = id

    @login_manager.user_loader
    def load_user(user_id):
        return User(user_id)

    @app.route('/login')
    def login():
        user = User(1)
        login_user(user)
        return 'Logged in'
    ```

## Flask-WTF

* **Description:** Flask-WTF integrates WTForms with Flask, providing form handling and validation. It simplifies form creation and security.
* **Links:**
    * [Flask-WTF Documentation](https://flask-wtf.readthedocs.io/en/latest/)
    * [Flask-WTF PyPI](https://pypi.org/project/Flask-WTF/)
* **Example Implementation:**

    ```python
    from flask import Flask, render_template, request
    from flask_wtf import FlaskForm
    from wtforms import StringField, SubmitField
    from dotenv import load_dotenv

    load_dotenv()  # Load variables from .env file

    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

    class MyForm(FlaskForm):
        name = StringField('Name')
        submit = SubmitField('Submit')

    @app.route('/', methods=['GET', 'POST'])
    def index():
        form = MyForm()
        if form.validate_on_submit():
            return f'Hello, {form.name.data}!'
        return render_template('index.html', form=form)
    ```

    ```python
    # .ENV example
    SECRET_KEY=f8a7e3b9c1d8e5f2
    ```

    ```python
    # .gitignore example. To make sure the .ENV file is never added to your repo
    .ENV
    ```

## Flask-Bcrypt

* **Description:** Flask-Bcrypt provides bcrypt password hashing for Flask. It's used for secure password storage.
* **Links:**
    * [Flask-Bcrypt Documentation](https://flask-bcrypt.readthedocs.io/en/latest/)
    * [Flask-Bcrypt PyPI](https://pypi.org/project/Flask-Bcrypt/)
* **Example Implementation:**

    ```python
    from flask import Flask
    from flask_bcrypt import Bcrypt

    app = Flask(__name__)
    bcrypt = Bcrypt(app)

    password = 'mysecretpassword'
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # To check the password
    # if bcrypt.check_password_hash(hashed_password, password):
    #     print("Password matches")
    ```

## PeeWee

* **Description:** Peewee is a lightweight Python ORM (Object-Relational Mapper) that simplifies database interactions by mapping Python classes to database tables.

* **Links:**
    * [PeeWee Documentation](https://docs.peewee-orm.com/en/latest/)
    * [Flask-Bcrypt PyPi](https://pypi.org/project/peewee/)
* **Example Implementation:**

```python
# models.py
import datetime
from peewee import *
from playhouse.postgres_ext import PostgresqlExtDatabase

# Custom model database that will use the existing connection
class CustomPostgresDatabase(PostgresqlExtDatabase):
    def __init__(self, db_wrapper, *args, **kwargs):
        self.db_wrapper = db_wrapper
        # Initialize with None values, we'll use the existing connection
        super().__init__(None, *args, **kwargs)
    
    def _connect(self, *args, **kwargs):
        # Return the existing connection
        return self.db_wrapper.connection
    
    def execute_sql(self, sql, params=None, commit=True):
        # Use the connection from the wrapper
        return self.db_wrapper.execute(sql, params)

# This will be set later when we have access to the database connection
db = None

# Define the base model
class BaseModel(Model):
    class Meta:
        database = db  # This will be set after db initialization

# Define the Pokemon model
class Pokemon(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField(max_length=100, unique=True)
    type = CharField(max_length=50)
    created_at = DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return f"Pokemon({self.id}, {self.name}, ({self.type})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @classmethod
    def create_tables(cls):
        # Create tables if they don't exist
        db.create_tables([cls], safe=True)
    
    @classmethod
    def find_by_id(cls, pokemon_id):
        try:
            return cls.get_by_id(pokemon_id)
        except cls.DoesNotExist:
            return None
    
    @classmethod
    def find_by_name(cls, name):
        try:
            return cls.get(cls.name == name)
        except cls.DoesNotExist:
            return None
    
    @classmethod
    def find_by_type(cls, type):
        return list(cls.select().where(cls.type == type))
    
    @classmethod
    def get_all(cls):
        return list(cls.select())


# app.py
from flask import Flask, jsonify, request
from database_connection import get_flask_database_connection
from models import CustomPostgresDatabase, db, BaseModel, Pokemon

app = Flask(__name__)

@app.before_request
def before_request():
    # Get the database connection
    connection = get_flask_database_connection(app)
    
    # Initialize the Peewee database with our connection
    global db
    if db is None:
        db = CustomPostgresDatabase(connection)
        
        # Set the database for the BaseModel
        BaseModel._meta.database = db
        
        # Create tables if they don't exist
        Pokemon.create_tables()

# Routes
@app.route('/pokemon', methods=['GET'])
def get_all_pokemon():
    pokemon_list = Pokemon.get_all()
    return jsonify([
        {"id": p.id, "name": p.name, "type": p.type} 
        for p in pokemon_list
    ])

@app.route('/pokemon/<int:pokemon_id>', methods=['GET'])
def get_pokemon(pokemon_id):
    pokemon = Pokemon.find_by_id(pokemon_id)
    if not pokemon:
        return jsonify({"error": f"Pokemon with ID {pokemon_id} not found"}), 404
    return jsonify({
        "id": pokemon.id,
        "name": pokemon.name,
        "type": pokemon.type
    })

@app.route('/pokemon', methods=['POST'])
def create_pokemon():
    data = request.get_json()
    
    if not data or 'name' not in data or 'type' not in data:
        return jsonify({"error": "Name and type are required"}), 400
    
    try:
        pokemon = Pokemon.create(
            name=data['name'],
            type=data['type']
        )
        return jsonify({
            "id": pokemon.id,
            "name": pokemon.name,
            "type": pokemon.type
        }), 201
    except IntegrityError:
        return jsonify({"error": f"Pokemon with name '{data['name']}' already exists"}), 400


if __name__ == '__main__':
    app.run(
        debug=True, 
        port=int(os.environ.get('PORT', 5001))
    )
```

## Bootstrap

* **Description:** Bootstrap is a popular CSS framework for developing responsive and mobile-first websites. It provides pre-built CSS and JavaScript components for easy web development.
* **Links:**
    * [Bootstrap Documentation](https://getbootstrap.com/)
    * [Bootstrap GitHub](https://github.com/twbs/bootstrap)
* **Usage in Flask:**
    * Include Bootstrap CSS and JavaScript files in your HTML templates.
    * Use Bootstrap classes to style your HTML elements.
    * Example using CDN links inside your HTML `<head>` tag.
    ```html
    <link rel="stylesheet" href="[https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css](https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css)">
    <script src="[https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js](https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js)"></script>
    ```
    * Or, download the files and include them locally.
* **Bootstrap Login Form (MUI-like):**

    Here's an example of a Bootstrap login form that aims to mimic the clean, minimalist style of Material UI (MUI).

    <img src="example_bootstrap_login_form.png" alt="Login form with bootstrap" style="width: 65%;">


    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login</title>
        <link rel="stylesheet" href="[https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css](https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css)">
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                background-color: #f8f9fa; /* Light background */
            }
            .form-container {
                width: 350px;
                padding: 30px;
                background-color: #ffffff; /* White form background */
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow */
            }
            .form-group label {
              font-weight: 500;
              margin-bottom: 5px;
            }
            .form-control{
              border-radius: 6px;
              padding: 10px;
              border: 1px solid #ced4da;
            }
            .btn-primary{
              width: 100%;
              padding: 12px;
              border-radius: 6px;
              background-color: #007bff;
              border: none;
            }
            .btn-primary:hover{
              background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="form-container">
            <h2 class="text-center mb-4">Login</h2>
            <form>
                <div class="form-group">
                    <label for="username">Username</label>
                    <input type="text" class="form-control" id="username" placeholder="Enter username">
                </div>
                <div class="form-group">
                    <label for="password">Password</label>
                    <input type="password" class="form-control" id="password" placeholder="Enter password">
                </div>
                <button type="submit" class="btn btn-primary">Login</button>
            </form>
        </div>
        <script src="[https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js](https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js)"></script>
    </body>
    </html>
    ```

