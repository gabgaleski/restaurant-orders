from src.models.ingredient import Ingredient, Restriction


# Req 1
def test_ingredient():
    ingredient = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("queijo mussarela")
    ingredient4 = Ingredient("farinha")
    assert ingredient.name == "queijo mussarela"
    assert ingredient.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }
    assert hash(ingredient) == hash(ingredient2)
    assert hash(ingredient) != hash(ingredient4)
    assert ingredient == ingredient2
    assert ingredient != ingredient4
    assert repr(ingredient) == "Ingredient('queijo mussarela')"
