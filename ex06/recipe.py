import os

cookbook = {
    "sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },
    "cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    }
}


def print_recipe(recipe_name: str):
    print(recipe_name)
    for key, value in cookbook[recipe_name].items():
        if key == "prep_time":
            print("preparation time: ", end="")
        else:
            print(key + ": ", end="")
        if key == "ingredients":
            print(", ".join(value))
        elif key == "prep_time":
            print(value, "minutes")
        else:
            print(value)
    print()


def print_cookbook(cook_book: dict):
    for recipe in cook_book:
        print_recipe(recipe)


def delete_recipe(recipe_name: str):
    print(f" Are you sure to delete  : \"{recipe_name}\" (YES to delete).")
    security = input(" : ")
    if security == "YES":
        try:
            del cookbook[recipe_name]
            print(f"Recipe for \"{recipe_name}\" is definytively removed .")
        except KeyError:
            print(f"Recipe \"{recipe_name}\" not found ")


def add_recipe(recipe_name: str, ingredients: list, meal: str, prep_time: int):
    cookbook[recipe_name] = {
        "ingredients": ingredients,
        "meal": meal,
        "prep_time": prep_time
    }
    print(f"Recipe for \"{recipe_name}\" added successfully")


def principal():
    menu = (
        "Please select an option by typing the corresponding number:\n"
        "1: Add a recipe\n"
        "2: Delete a recipe\n"
        "3: Print a recipe\n"
        "4: Print the cookbook\n"
        "5: Quit\n"
    )
    wrong_input = (
        "This option does not exist, please type the corresponding number.\n"
        "To exit, enter 5.\n"
    )
    os.system("clear")
    while True:
        print(menu)
        answer = input()
        while not (answer > '0' and answer < '6'):
            os.system("clear")
            print(menu)
            print(wrong_input)
            answer = input()
        # choosing menu options
        if answer == "1":
            new_name = input("Recipe name:\n")
            new_ing = input("Ingredients list (separated by , )\n").split(",")
            new_meal = input("Meal type:\n")
            time_ok = False
            while not time_ok:
                str_new_time = input("Preparation time (in minutes):\n")
                if str_new_time.isdigit():
                    time_ok = True
                    new_time = int(str_new_time)
                else:
                    print("Not a number. Try again\n")
            add_recipe(new_name, new_ing, new_meal, new_time)
        elif answer == "2":
            recipe_name = input("Recipe's name to delete?\n")
            delete_recipe(recipe_name)
        elif answer == "3":
            name = input("Please enter the recipe's name\
                to get its details:?\n")
            try:
                print_recipe(name)
            except KeyError:
                print(f"Recipe \"{name}\" not found ")
        elif answer == "4":
            print_cookbook(cookbook)
        elif answer == "5":
            print("Cookbook closed.")
            break


if __name__ == "__main__":
    principal()
