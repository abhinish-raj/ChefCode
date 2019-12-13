#
# n = int(input())
# ingredients = list(map(str, input().rstrip().split()))
n = 5
ingredients = list(("FATOil","FATCheese","FATEgg"," FIBERSpinach" , "CARBRice", " FIBERBeans"))
# here i stand for ingredients that contains the respective FAT, FIBER, CARBS
FATIngrident = FIBERIngrident = CARBIngrident = totalIngredients = 0
refrigerator = list(ingredients)
chef_working_day = ""

for ingredient in ingredients:
    print("Before for loop current : {}\n".format(refrigerator))
    if "FAT" in ingredient:
        FATIngrident += 1
        totalIngredients += 1
        if totalIngredients >= 3 and FATIngrident >= 2:

            # prepare the dish
            # POP the 2 common ingredient
            for ingre in ingredients:
                if "FAT" in ingre:
                    # print(refrigerator.pop(refrigerator.index(ingre)))
                    refrigerator.pop(refrigerator.index(ingre))
                    FATIngrident -= 1
            temp = refrigerator.pop(0)
            if "FIBER" in temp:
                FIBERIngrident -= 1
            elif "CARB" in temp:
                CARBIngrident -= 1
            chef_working_day += "1"
        else:
            chef_working_day += "0"
    elif "FIBER" in ingredient:
        FIBERIngrident += 1
        totalIngredients += 1
        if totalIngredients >= 3 and FIBERIngrident >= 2:
            # prepare the dish
            ##
            for ingre in ingredients:
                if "FIBER" in ingre:
                    # print(refrigerator.pop(refrigerator.index(ingre)))
                    refrigerator.pop(refrigerator.index(ingre))
                    FIBERIngrident -= 1
            temp = refrigerator.pop(0)
            if "FAT" in temp:
                FIBERIngrident -= 1
            elif "CARB" in temp:
                CARBIngrident -= 1
            chef_working_day += "1"
        else:
            chef_working_day += "0"
    elif "CARB" in ingredient:
        CARBIngrident += 1
        totalIngredients += 1
        if totalIngredients >= 3 and CARBIngrident >= 2:
            # prepare the dish
            for ingre in ingredients:
                if "CARB" in ingre:
                    # print(refrigerator.pop(refrigerator.index(ingre)))
                    refrigerator.pop(refrigerator.index(ingre))
                    CARBIngrident -= 1
            temp = refrigerator.pop(0)
            if "FIBER" in temp:
                FIBERIngrident -= 1
            elif "FAT" in temp:
                CARBIngrident -= 1
            chef_working_day += "1"
        else:
            chef_working_day += "0"

print( "This is FATIngrident {} \nTHis is FIBERIngrident {} \nThis is CARBIngrident {}\n Ingredient List : {} \n "
       "Refrigerator List : {} \n Chef Working Day : {} \n".format(
        FATIngrident, FIBERIngrident, CARBIngrident, ingredients, refrigerator, chef_working_day))
