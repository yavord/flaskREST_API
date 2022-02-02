import requests
import pprint

def __output_get():
    pass

def fetchRecipes(url = 'http://127.0.0.1:3000/recipes'):
    response = requests.get(url)
    data = response.json()
    
    print('Response body (JSON):')
    pprint.pprint(data)
    print('Status: ' + str(response.status_code))

def fetchIngredients(url = 'http://127.0.0.1:3000/recipes/details/', recipe = 'chai'):
    response = requests.get(url+recipe)
    data = response.json()

    print('Response body (JSON):')
    pprint.pprint(data)
    print('Status: ' + str(response.status_code))

def addRecipe(url = 'http://127.0.0.1:3000/recipes', recipe={'test1':'test2'}):
    response = requests.post(url=url, data=recipe)


### TEST
# fetchRecipes()
# fetchIngredients(recipe='garlicPasta')
addRecipe()