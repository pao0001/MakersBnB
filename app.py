import os
from flask import Flask, request, redirect, render_template, abort, url_for, flash
from flask_mail import Mail, Message
from lib.database_connection import get_flask_database_connection
from lib.property_repository import PropertyRepository
from lib.property import Property

# Create a new Flask app
app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'giulianopaolini1991@gmail.com'
app.config['MAIL_PASSWORD'] = 'ioyisepfpeakqvci'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.secret_key = '02z[^=~3F(qL'

mail = Mail(app)

# == Your Routes Here ==

# MAIL APP
@app.route('/property_request', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        from_date = request.form['from_date']
        to_date = request.form['to_date']

        if not name or not email or not message:
            flash('All fields are required.', 'warning')
            return redirect('/property_request')

        try:
            msg = Message('Contact Form Submission', 
                sender='giulianopaolini1991@gmail.com',  
                recipients=['giulianopaolini1991@gmail.com'])
            msg.body = f"Name: {name}\nUser Email: {email}\nFrom: {from_date}\nTo: {to_date}\n\nMessage:\n{message}"
            mail.send(msg)
            flash('Message sent successfully!', 'success')
        except Exception as e:
            flash(f'Failed to send message. Error: {str(e)}', 'danger')
        return redirect('/property_request')

    return render_template('property_request.html')

# END MAIL APP


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

#
@app.route('/create-property', methods=['GET'])
def get_create_property():
    return render_template('create-property.html')


# Create a new property
@app.route('/', methods=['POST'])
def create_property():
    connection = get_flask_database_connection(app)
    repository = PropertyRepository(connection)


    name = request.form['name']
    email = request.form['email']
    phone_number = request.form['phone_number']
    address = request.form['address']
    description = request.form['description']
    price_per_night = request.form['price_per_night']
    availability = request.form['availability']
    user_id = request.form['user_id']

    new_property = Property(None, name, email, phone_number, 
        address, description, price_per_night, 
        availability, user_id
        )
    
    # if not property.is_valid():
    #     return render_template('/create-property.html', new_property=new_property, errors=new_property.generate_errors()), 400

    new_property = repository.create(new_property)
    return redirect (f'/{new_property.id}')

# Delete a property from property list
@app.route('/delete/<int:property_id>', methods=['POST'])
def delete_property(property_id):
    connection = get_flask_database_connection(app)
    repository = PropertyRepository(connection)
    repository.delete(property_id)
    return redirect(url_for('get_index'))

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
