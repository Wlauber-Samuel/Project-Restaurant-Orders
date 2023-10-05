from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient_butter = Ingredient("manteiga")
    ingredient_butter02 = Ingredient("manteiga")
    ingredient_shrimp = Ingredient("camarão")

    assert ingredient_butter.name == "manteiga"
    assert ingredient_butter.restrictions == {"LACTOSE", "ANIMAL_DERIVED"}
    assert ingredient_shrimp.name == "camarão"
    assert ingredient_shrimp.restrictions == {
        "ANIMAL_MEAT", "ANIMAL_DERIVED", "SEAFOOD"}
    assert ingredient_butter02.name == "manteiga"
    assert ingredient_butter02.restrictions == {"LACTOSE", "ANIMAL_DERIVED"}

    assert type(ingredient_butter.__hash__()) == int
    assert type(ingredient_shrimp.__hash__()) == int
    assert ingredient_butter.__hash__() == ingredient_butter02.__hash__()
    assert ingredient_butter.__hash__() != ingredient_shrimp.__hash__()
    assert ingredient_butter.__eq__(ingredient_butter02) == True
    assert ingredient_butter.__eq__(ingredient_shrimp) == False
    assert ingredient_shrimp.__eq__(ingredient_butter) == False
    assert ingredient_butter.__repr__() == "ingredient(manteiga)"
    assert ingredient_shrimp.__repr__() == "ingredient(camarão)"
