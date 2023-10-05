import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    dish = Dish("Lasanha", 35.0)
    dish2 = Dish("Lasanha", 35.0)
    dish3 = Dish("Pizza", 25.0)
    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("molho de tomate")
    assert dish.name == "Lasanha"
    assert dish.price == 35.0
    assert dish.recipe == {}
    assert repr(dish) == "Dish('Lasanha', R$35.00)"
    assert dish == dish2
    assert dish != dish3
    assert hash(dish) == hash(dish2)
    assert hash(dish) != hash(dish3)

    dish.add_ingredient_dependency(ingredient1, 200)
    dish.add_ingredient_dependency(ingredient2, 500)
    assert dish.recipe == {ingredient1: 200, ingredient2: 500}

    assert dish.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }
    assert dish.get_ingredients() == {ingredient1, ingredient2}

    with pytest.raises(TypeError):
        Dish("Lasanha", "35.0")

    with pytest.raises(ValueError):
        Dish("Lasanha", -35.0)
