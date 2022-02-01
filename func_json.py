import json

def __get_recipes():
    with open('data.json') as json_f:
        return((json.load(json_f))['recipes'])

def get_recipe_names():
    data = __get_recipes()
    recipeNames = {'recipeNames':[]}
    for recipe in range(len(data)):
        recipeNames['recipeNames'].append(data[recipe]['name'])
    return(recipeNames)

def get_ingredients(x):
    data = __get_recipes()
    details = {}
    for recipe in range(len(data)):
        if x == data[recipe]['name']:
            ingredients = data[recipe]['ingredients']
            details['details'] = {
                "ingredients" : ingredients,
                'numsteps' : len(ingredients)
            }
    return(details)

def add_recipe():
    # data = __get_recipes()
    print('success')
    return('')

### TEST
# print(get_recipe_names())
# print(get_ingredients('chai'))