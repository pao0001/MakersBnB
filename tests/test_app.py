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
def test_get_property(db_connection, page, test_web_address):
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

    # # We look at all the <li> tags
    # list_items = page.locator("p")

    # # We assert that it has the books in it
    # expect(list_items).to_have_text([
    #     "Invisible Cities by Italo Calvino",
    #     "The Man Who Was Thursday by GK Chesterton",
    #     "Bluets by Maggie Nelson",
    #     "No Place on Earth by Christa Wolf",
    #     "Nevada by Imogen Binnie",
    # ])