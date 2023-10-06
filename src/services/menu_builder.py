from typing import Dict, List

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> List[Dict]:
        filtered_list = []
        while len(self.menu_data.dishes) > 0:
            new_item = {}

            dish = self.menu_data.dishes.pop()
            recipe = dish.recipe
            ingredients = recipe.keys()

            new_item["dish_name"] = dish.name
            new_item["price"] = dish.price
            new_item["ingredients"] = set()
            new_item["restrictions"] = set()

            for ingredient in ingredients:
                new_item["ingredients"].add(ingredient)
                new_item["restrictions"].update(ingredient.restrictions)

            if restriction in new_item["restrictions"]:
                continue
            if not self.inventory.check_recipe_availability(recipe):
                continue
            filtered_list.append(new_item)
        return filtered_list
