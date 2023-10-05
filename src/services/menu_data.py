# Req 3
import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        with open(source_path, encoding="utf8") as csvfile:
            reader = csv.reader(
                csvfile,
                delimiter=",",
            )

            head, *rows = reader
            for row in rows:
                dish_name, dish_price, ingredient_name, recipe_amount = row
                dish_price = float(dish_price)
                recipe_amount = int(recipe_amount)

                dish = None
                for d in self.dishes:
                    if d.name == dish_name:
                        dish = d
                        break

                if not dish:
                    dish = Dish(dish_name, dish_price)
                    self.dishes.add(dish)
                ingredient = Ingredient(ingredient_name)
                dish.add_ingredient_dependency(ingredient, recipe_amount)
