import os
from flask import Flask, request, redirect, render_template, abort, url_for, flash
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)
app.secret_key = '02z[^=~3F(qL'
# == Your Routes Here ==
@app.route('/<int:property_id>')
def show_property(property_id):
    connection = get_flask_database_connection(app)
    rows = connection.execute("SELECT * FROM properties WHERE id = %s", [property_id])

    if not rows:
        abort(404)

    property = rows[0]

    return render_template('property.html', property=property)

@app.route('/login', methods=['GET', 'POST'])
def login():
    from lib.password_authenticator import PasswordAuthenticator
    if request.method == 'POST':
        connection = get_flask_database_connection(app)
        email = request.form['email']
        password = request.form['password']
        user = PasswordAuthenticator(email, password, connection)
        if user.authenticate():
            flash('Login Successful', 'success')
            return redirect(url_for('get_index'))
        else:
            flash('Invalid email or password!', 'error')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/', methods=['GET'])
def get_index():
    connection = get_flask_database_connection(app)
    rows = connection.execute("SELECT * FROM properties")
    return render_template('index.html', properties=rows)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
