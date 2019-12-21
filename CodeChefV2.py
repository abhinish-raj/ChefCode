#
# n = int(input())
# ingredients = list(map(str, input().rstrip().split()))
n = 12
ingredients = ['FATOil', 'FIBERSpinach', 'CARBRice', 'FATCheese', 'FIBERBeans', 'FATEgg', 'FIBERBroccoIi', 'CARBPotato',
               'CARBCorn', 'FATOlive', 'FIBERCarrot', 'CARBBeetroot', 'FATOil', 'FIBERSpinach', 'CARBRice', 'FATCheese','FIBERBeans', 'FATEgg', 'FIBERBroccoIi', 'CARBPotato',
               'CARBCorn', 'FATOlive', 'FIBERCarrot', 'CARBBeetroot','FATOil', 'FIBERSpinach', 'CARBRice', 'FATCheese', 'FIBERBeans', 'FATEgg', 'FIBERBroccoIi', 'CARBPotato',
               'CARBCorn', 'FATOlive', 'FIBERCarrot', 'CARBBeetroot']
# here i stand for ingredients that contains the respective FAT, FIBER, CARBS
# FATIngrident = FIBERIngrident = CARBIngrident = totalIngredients = 0
storedI = dict({"FAT": 0, "FIBER": 0, "CARB": 0, "TOTAL": 0, "CHEFDAY": ""})
refrigerator = list(ingredients)

for ingredient in ingredients:
    print("Before for loop current : {}".format(refrigerator))
    print("ingredient {}".format(ingredient))
    if "FAT" in ingredient:
        storedI["FAT"] += 1
    elif "FIBER" in ingredient:
        storedI["FIBER"] += 1
    elif "CARB" in ingredient:
        storedI["CARB"] += 1
    storedI["TOTAL"] += 1

    """
    Check if there is necessary ingredient in the Refrigerator 
    need to check if there are minimum requirement present in fridge 
    need to check if there are minimum at least two of any flag in the fridge  
    """
    print(storedI["TOTAL"])
    if storedI["TOTAL"] >= 3:
        # Checking the ingredients
        count = 0
        if storedI["FAT"] >= 2:
            cook_food("FAT", storedI)
        elif storedI["FIBER"] >= 2:
            cook_food("FIBER", storedI)
        elif storedI["CARB"] >= 2:
            cook_food("CARB", storedI)
        else:
            storedI["CHEFDAY"] += "0"
    else:
        storedI["CHEFDAY"] += "0"


    def cook_food(ingredientType, storedI):
        # Finding the index of the ingredientTypes for poping them
        flag = 2

        for ingre in refrigerator:
            if flag > 0 and ingredientType in ingre:
                refrigerator.pop(refrigerator.index(ingre))
                flag -= 1
                storedI[ingredientType] -= 1

        if flag == 0:
            tmpI = refrigerator.pop(0)
            if "FAT" in tmpI:
                storedI["FAT"] -= 1
            elif "FIBER" in tmpI:
                storedI["FIBER"] -= 1
            elif "CARB" in tmpI:
                storedI["CARB"] -= 1
            storedI["TOTAL"] -= 3
            storedI["CHEFDAY"] += "1"

print("This is FATIngrident {} \nTHis is FIBERIngrident {} \nThis is CARBIngrident {}\n Ingredient List : {} \n "
      "Refrigerator List : {} \n Chef Working Day : {} \n Total Ingredient {} \n".format(
    storedI["FAT"], storedI["FIBER"], storedI["CARB"], ingredients, refrigerator, storedI["CHEFDAY"], storedI["TOTAL"]))

# if "FAT" in ingredient:
#     FATIngrident += 1
#     totalIngredients += 1
#     if totalIngredients >= 3 and FATIngrident >= 2:
#
#         # prepare the dish
#         # POP the 2 common ingredient
#         for ingre in ingredients:
#             if "FAT" in ingre:
#                 # print(refrigerator.pop(refrigerator.index(ingre)))
#                 refrigerator.pop(refrigerator.index(ingre))
#                 FATIngrident -= 1
#         temp = refrigerator.pop(0)
#         if "FIBER" in temp:
#             FIBERIngrident -= 1
#         elif "CARB" in temp:
#             CARBIngrident -= 1
#         chef_working_day += "1"
#     else:
#         chef_working_day += "0"
# elif "FIBER" in ingredient:
#     FIBERIngrident += 1
#     totalIngredients += 1
#     if totalIngredients >= 3 and FIBERIngrident >= 2:
#         # prepare the dish
#         ##
#         for ingre in ingredients:
#             if "FIBER" in ingre:
#                 # print(refrigerator.pop(refrigerator.index(ingre)))
#                 refrigerator.pop(refrigerator.index(ingre))
#                 FIBERIngrident -= 1
#         temp = refrigerator.pop(0)
#         if "FAT" in temp:
#             FIBERIngrident -= 1
#         elif "CARB" in temp:
#             CARBIngrident -= 1
#         chef_working_day += "1"
#     else:
#         chef_working_day += "0"
# elif "CARB" in ingredient:
#     CARBIngrident += 1
#     totalIngredients += 1
#     if totalIngredients >= 3 and CARBIngrident >= 2:
#         # prepare the dish
#         for ingre in ingredients:
#             if "CARB" in ingre:
#                 # print(refrigerator.pop(refrigerator.index(ingre)))
#                 refrigerator.pop(refrigerator.index(ingre))
#                 CARBIngrident -= 1
#         temp = refrigerator.pop(0)
#         if "FIBER" in temp:
#             FIBERIngrident -= 1
#         elif "FAT" in temp:
#             CARBIngrident -= 1
#         chef_working_day += "1"
#     else:
#         chef_working_day += "0"
"""
print( "This is FATIngrident {} \nTHis is FIBERIngrident {} \nThis is CARBIngrident {}\n Ingredient List : {} \n "
       "Refrigerator List : {} \n Chef Working Day : {} \n".format(
        FATIngrident, FIBERIngrident, CARBIngrident, ingredients, refrigerator, chef_working_day))
"""
