""" app/__init__.py """

from flask import Flask
from app.useraccounts import UserClass
from app.shoppinglist import ShoppinglistClass
from app.shoppingitems import ShoppingItemsClass


# Initialize the app
app = Flask(
    __name__, instance_relative_config=True)
app.secret_key = 'dresscodesleepbehappy'

user_object = UserClass()
shoplist_obj = ShoppinglistClass()
shopitems_obj = ShoppingItemsClass()

from app import views

# Load the config file
app.config.from_object('config')
