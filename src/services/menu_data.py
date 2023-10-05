from src.models.dish import Dish
from src.models.ingredient import Ingredient

import sys


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        file = self.read_file(source_path)
        self.add_ingredients_for_dishes(file)

    def read_file(self, path_file):
        if not path_file.endswith('.csv'):
            sys.stderr.write('Formato inválido\n')
            return None
        try:
            with open(path_file, 'r', encoding='utf-8') as file:
                file_lines = file.read().split("\n")
                return file_lines
        except FileNotFoundError:
            sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
            return None

    def add_ingredients_for_dishes(self, file):
        dishes = {}

        for index in range(1, len(file) - 1):
            dish_information = file[index].split(",")

            if dish_information[0] not in dishes:
                dishes[dish_information[0]] = Dish(
                    dish_information[0], float(dish_information[1]))

            new_ingredient = Ingredient(dish_information[2])
            dishes[dish_information[0]].add_ingredient_dependency(
                new_ingredient, int(dish_information[3]))

        if (file[len(file) - 2]):
            for dish in dishes.values():
                self.dishes.add(dish)
