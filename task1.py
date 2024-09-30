cook_book = {}

with open("recipes.txt", "r", encoding="utf-8") as file:
    while True:

        name_recipe = file.readline().rstrip()
        if not name_recipe:
            break
        count_ingredients = file.readline().rstrip()
        ingredients = []
        for _ in range(int(count_ingredients)):
            ingredient = file.readline().rstrip()
            name, quantity, measure = ingredient.split(" | ")
            ingredient = {"ingredient_name": name, "quantity": int(quantity), "measure": measure}
            ingredients.append(ingredient)
        file.readline()
        cook_book[name_recipe] = ingredients
