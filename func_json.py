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

def __check_if_exists(data, post):
    return(any(item == post for item in data))

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
    data = __get_recipes()
    error = {"error": "Recipe already exists"}
    check = __check_if_exists(data=data, post=x)
    if check == True:
        return(error, 400)
    elif check == False:
        __write_recipe(x)
        return("",201)

### TEST
# print(get_recipe_names())
# print(get_ingredients('chai'))
# __recipe_post = {"name": "butteredBagel", 
#     "ingredients": ["1 bagel","butter"], 
# 	"instructions": ["cut the bagel", "spread butter on bagel"] 
# }
# add_recipe(__recipe_post)