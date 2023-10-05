from src.models.ingredient import Ingredient
from src.models.ingredient import Restriction


# Req 1
def test_ingredient():
    ingredient_butter = Ingredient("manteiga")
    ingredient_butter02 = Ingredient("manteiga")
    ingredient_shrimp = Ingredient("camarão")

    assert ingredient_butter.name == "manteiga"
    assert ingredient_butter.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED
    }
    assert ingredient_shrimp.name == "camarão"
    assert ingredient_shrimp.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
        Restriction.SEAFOOD
    }
    assert ingredient_butter02.name == "manteiga"
    assert ingredient_butter02.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED
    }

    assert type(ingredient_butter.__hash__()) == int
    assert type(ingredient_shrimp.__hash__()) == int
    assert ingredient_butter.__hash__() == ingredient_butter02.__hash__()
    assert ingredient_butter.__hash__() != ingredient_shrimp.__hash__()
    assert ingredient_butter.__eq__(ingredient_butter02) is True
    assert ingredient_butter.__eq__(ingredient_shrimp) is False
    assert ingredient_shrimp.__eq__(ingredient_butter) is False
    assert ingredient_butter.__repr__() == "Ingredient('manteiga')"
    assert ingredient_shrimp.__repr__() == "Ingredient('camarão')"
