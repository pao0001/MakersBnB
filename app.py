import os
from flask import Flask, request, render_template, abort, redirect
from lib.database_connection import get_flask_database_connection
from lib.property_repository import PropertyRepository
from lib.property import Property

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/<int:property_id>')
def show_property(property_id):
    connection = get_flask_database_connection(app)
    rows = connection.execute("SELECT * FROM properties WHERE id = %s", [property_id])

    if not rows:
        abort(404)

    property = rows[0]

    return render_template('property.html', property=property)

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


# Create a new 
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


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
