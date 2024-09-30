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


def get_shop_list_by_dishes(dishes: list, person_count: int) -> dict:
    lst_ingredients = {}
    for dish in dishes:
        for count_ingredient in cook_book[dish]:
            if count_ingredient["ingredient_name"] in lst_ingredients:
                lst_ingredients[count_ingredient["ingredient_name"]]["quantity"] += \
                    count_ingredient["quantity"] * person_count
            else:
                lst_ingredients[count_ingredient["ingredient_name"]] = \
                    {"measure": count_ingredient["measure"],
                     "quantity": count_ingredient["quantity"] * person_count}
    return lst_ingredients


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
