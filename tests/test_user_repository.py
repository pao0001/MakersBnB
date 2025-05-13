from lib.user_repository import *
from lib.user import *


def test_all(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")