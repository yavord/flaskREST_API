from urllib import response
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

def fetchIngredients(recipe = 'chai', url = 'http://127.0.0.1:3000/recipes/details/'):
    response = requests.get(url+recipe)
    data = response.json()

    print('Response body (JSON):')
    pprint.pprint(data)
    print('Status: ' + str(response.status_code))

def addRecipe(url = 'http://127.0.0.1:3000/recipes'):
    pass


### TEST
# fetchRecipes()
# fetchIngredients(recipe='garlicPasta')