from src.models.dish import Dish
from src.models.ingredient import Ingredient
from src.models.ingredient import Restriction

import pytest


# Req 2
def test_dish():
    ingredient_shrimp = Ingredient("camarão")
    ingredient_butter = Ingredient("manteiga")

    with pytest.raises(TypeError, match="Dish price must be float."):
        invalid_price_type = Dish("Lasanha", "12.90")
    with pytest.raises(ValueError, match="Dish price must be greater then zero."):
        invalid_price_value = Dish("Lasanha", -12.90)

    lasanha = Dish("Lasanha", 12.90)
    feijoada = Dish("Feijoada", 20.90)

    assert lasanha.name == "Lasanha"
    assert lasanha.price == 12.90
    assert len(lasanha.recipe) == 0
    assert feijoada.name == "Feijoada"
    assert feijoada.price == 20.90
    assert len(feijoada.recipe) == 0

    assert lasanha.__repr__() == "Dish('Lasanha', R$12.90)"
    assert feijoada.__repr__() == "Dish('Feijoada', R$20.90)"
    assert lasanha.__eq__(lasanha) == True
    assert lasanha.__eq__(feijoada) == False
    assert feijoada.__eq__(feijoada) == True
    assert feijoada.__eq__(lasanha) == False
    assert type(lasanha.__hash__()) == int
    assert type(feijoada.__hash__()) == int
    assert lasanha.__hash__() != feijoada.__hash__()
    assert lasanha.__hash__() == lasanha.__hash__()
    assert feijoada.__hash__() == feijoada.__hash__()
    assert feijoada.__hash__() != lasanha.__hash__()

    lasanha.add_ingredient_dependency(ingredient_butter, 2)
    lasanha.add_ingredient_dependency(ingredient_shrimp, 10)
    assert len(lasanha.recipe) == 2
    assert lasanha.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
        Restriction.LACTOSE,
        Restriction.SEAFOOD
    }
    assert lasanha.get_ingredients() == {
        ingredient_butter,
        ingredient_shrimp
    }

    feijoada.add_ingredient_dependency(ingredient_butter, 1)
    assert len(feijoada.recipe) == 1
    assert feijoada.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.LACTOSE
    }
    assert feijoada.get_ingredients() == {
        ingredient_butter
    }
