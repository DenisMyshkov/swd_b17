import pytest


def test_19(app):
    app.add_3_duck_in_cart()
    app.remove_all_products_from_cart()
