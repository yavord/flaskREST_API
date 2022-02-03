import requests
import pprint
import json


__recipe_post = {"name": "butteredBagel", 
    "ingredients": ["1 bagel","butter"], 
	"instructions": ["cut the bagel", "spread butter on bagel"] 
}

def __output_get(json_data, status_code):
    print('Response body (JSON):')
    pprint.pprint(json_data)
    print('Status: ' + str(status_code))

def fetchRecipes(url = 'http://127.0.0.1:3000/recipes'):
    response = requests.get(url)
    data = response.json()
    __output_get(data, response.status_code)

def fetchIngredients(url = 'http://127.0.0.1:3000/recipes/details/', recipe = 'chai'):
    response = requests.get(url+recipe)
    data = response.json()
    __output_get(data, response.status_code)

def addRecipe(url = 'http://127.0.0.1:3000/recipes', recipe=__recipe_post):
    response = requests.post(
        url=url, 
        data=json.dumps(recipe), 
        headers={"Content-Type": "application/json"}
    )

    if response.status_code == 201:
        print('Response body (JSON): ' + str(response.text))
        print('Status: ' + str(response.status_code))
    elif response.status_code == 400:
        __output_get(response.text, response.status_code)

### TEST
# fetchRecipes()
# fetchIngredients(recipe='garlicPasta')
addRecipe()