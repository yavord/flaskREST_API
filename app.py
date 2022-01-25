from glob import escape
import json
from flask import Flask, jsonify
import func_json


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>See: /recipes, /recipes/details/#recipeName#</p>"

@app.route("/recipes")
def show_recipes():
    return jsonify(func_json.get_recipe_names())

@app.route("/recipes/details/<string:recipe>")
def show_ingredients(recipe):
    return jsonify(func_json.get_ingredients(f'{escape(recipe)}'))