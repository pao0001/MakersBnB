from playwright.sync_api import Page, expect

# Tests for your routes go here

# """
# We can render the index page
# """
# def test_get_index(page, test_web_address):
#     # We load a virtual browser and navigate to the /index page
#     page.goto(f"http://{test_web_address}/index")

#     # We look at the <p> tag
#     p_tag = page.locator("p")

#     # We assert that it has the text "This is the homepage."
#     expect(p_tag).to_have_text("This is the homepage.")

"""
Test route to a single property page
"""
def test_show_property(db_connection, page, test_web_address):
    # We seed our database with the properties seed file
    db_connection.seed("seeds/bnb_seed.sql")

    # We load a virtual browser and navigate to the /<int:property_id> page
    page.goto(f"http://{test_web_address}/")

    page.click("text=A lovely place to stay.")

    title_element = page.locator(".t-name")
    expect(title_element).to_have_text("Name: John Doe")

    title_element = page.locator(".t-email")
    expect(title_element).to_have_text("Email: johndoe@bing.com")

    title_element = page.locator(".t-phone_number")
    expect(title_element).to_have_text("Phone Number: 1234567890")

    title_element = page.locator(".t-address")
    expect(title_element).to_have_text("Address: 123 Main St, Cityville")

    title_element = page.locator(".t-description")
    expect(title_element).to_have_text("Description: A lovely place to stay.")

    title_element = page.locator(".t-price_per_night")
    expect(title_element).to_have_text("Price per night: 100.00")

    title_element = page.locator(".t-availability")
    expect(title_element).to_have_text("Availability: available")

    title_element = page.locator(".t-user_id")
    expect(title_element).to_have_text("UserID: 1")


def test_create_property(db_connection, page, test_web_address):
    # We seed our database with the properties seed file
    db_connection.seed("seeds/bnb_seed.sql")

    page.goto(f"http://{test_web_address}/")
    page.click("text=here")

    page.fill("input[name='name']", "cindy")
    page.fill("input[name='email']", "cindy@ymail.co")
    page.fill("input[name='phone_number']", "95849253")
    page.fill("input[name='address']", "478 Pinetree Cove")    
    page.fill("input[name='description']", "A rustic cottage")
    page.fill("input[name='price_per_night']", "9000")
    page.fill("input[name='availability']", "unavailable")
    page.fill("input[name='user_id']", "1")    

    page.click('input[value="Create Property"]')


    title_element = page.locator(".t-name")
    expect(title_element).to_have_text("Name: cindy")

    title_element = page.locator(".t-email")
    expect(title_element).to_have_text("Email: cindy@ymail.co")

    title_element = page.locator(".t-phone_number")
    expect(title_element).to_have_text("Phone Number: 95849253")

    title_element = page.locator(".t-address")
    expect(title_element).to_have_text("Address: 478 Pinetree Cove")

    title_element = page.locator(".t-description")
    expect(title_element).to_have_text("Description: A rustic cottage")

    title_element = page.locator(".t-price_per_night")
    expect(title_element).to_have_text("Price per night: 9000.00")

    title_element = page.locator(".t-availability")
    expect(title_element).to_have_text("Availability: unavailable")

    title_element = page.locator(".t-user_id")
    expect(title_element).to_have_text("UserID: 1")

"""
When we delete a property. the property will be removed from property list page
"""

def test_delete_book(db_connection, page, test_web_address):
    db_connection.seed("seeds/bnb_seed.sql")
    page.goto(f"http://{test_web_address}/")
    current_property_for_delete = page.locator("text=A lovely place to stay.")
    expect(current_property_for_delete).to_be_visible()
    page.click("text=A lovely place to stay.")
    page.once("dialog", lambda dialog: dialog.accept())
    page.click("text=Delete Property")
    lakehouse_description = page.locator("text=Peaceful lake house with mountain views.")
    expect(lakehouse_description).to_be_visible()
    deleted_property = page.locator("text=A lovely place to stay.")
    expect(deleted_property).not_to_be_visible()

# """
# When a property is updated via update method, the property list will display the changes
# """

# def test_update_book(db_connection, page, test_web_address):
#     db_connection.seed("seeds/bnb_seed.sql")
#     page.goto(f"http://{test_web_address}/")
#     page.click("text=A lovely place to stay.")

