import json

def __get_recipes():
    with open('data.json') as json_f:
        return((json.load(json_f))['recipes'])

def __write_recipe(recipe):
    with open('data.json', 'r+') as json_f:
        file_data = json.load(json_f)
        file_data['recipes'].append(recipe)
        json_f.seek(0)
        json.dump(file_data, json_f, indent=2)

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

def add_recipe(x):
    __write_recipe(x)
    print('writing complete')

### TEST
# print(get_recipe_names())
# print(get_ingredients('chai'))