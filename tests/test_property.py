from lib.property import *

"""
Test Property constructs with the following:
id
name
availability
price_per_night
email
phone_number
address
description
user_id
"""

def test_property_for_construction():
    property = Property(
        4,
        "Sunny Shack",
        "example@example.com",
        "012347656894",
        "4 Sunny Street, Sunny Town, SU00 SU2",
        "This is a wonderful sunny spot in the heart of Sunny Town",
        "£5.99",
        True,
        32
    )

    assert property.id == 4
    assert property.name == "Sunny Shack"
    assert property.email == "example@example.com"
    assert property.phone_number == "012347656894"
    assert property.address == "4 Sunny Street, Sunny Town, SU00 SU2"
    assert property.description == "This is a wonderful sunny spot in the heart of Sunny Town"
    assert property.price_per_night == "£5.99"
    assert property.availability == True
    assert property.user_id == 32

    """
    Test variables are equal to themselves
    """

def test_variables_equal_themselves():
    property1 = Property(
        4,
        "Sunny Shack",
        "example@example.com",
        "012347656894",
        "4 Sunny Street, Sunny Town, SU00 SU2",
        "This is a wonderful sunny spot in the heart of Sunny Town",
        "£5.99",
        True,
        32
    )

    property2 = Property(
        4,
        "Sunny Shack",
        "example@example.com",
        "012347656894",
        "4 Sunny Street, Sunny Town, SU00 SU2",
        "This is a wonderful sunny spot in the heart of Sunny Town",
        "£5.99",
        True,
        32
    )

    assert property1 == property2

    """
    Test the Property gets formatted nicely
    """

def test_property_formats_nicely():
    property1 = Property(
        4,
        "Sunny Shack",
        "example@example.com",
        "012347656894",
        "4 Sunny Street, Sunny Town, SU00 SU2",
        "This is a wonderful sunny spot in the heart of Sunny Town",
        "£5.99",
        True,
        32
    )

    assert str(property1) == (
        "Property(4, Sunny Shack, example@example.com, 012347656894, "
        "4 Sunny Street, Sunny Town, SU00 SU2, "
        "This is a wonderful sunny spot in the heart of Sunny Town, "
        "£5.99, True, 32)"
    )
        