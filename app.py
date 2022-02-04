from markupsafe import escape
from flask import Flask, jsonify, request
import func_json


app = Flask(__name__)

@app.route("/")
def home():
    return "<p>See: /recipes, /recipes/details/#recipeName#</p>"

@app.route("/recipes", methods=['GET','POST', 'PUT'])
def recipes():
    if request.method == 'POST':
        return func_json.add_recipe(request.get_json())
    elif request.method == 'PUT':
        return func_json.update_recipe(request.get_json())
    elif request.method == 'GET':
        return jsonify(func_json.get_recipe_names())
    
@app.route("/recipes/details/<string:recipe>")
def show_ingredients(recipe):
    return jsonify(func_json.get_ingredients(f'{escape(recipe)}'))