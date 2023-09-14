class Burger:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def print(self):
        print(self.ingredients)

class BurgerFactory:

    def createCheeseBurger(self):
        ingredients = ["bun", "cheese", "Aalo-patty"]
        return Burger(ingredients)

    def createDulexChesseBurger(self):
        ingredients = ["bun", "tomato", "lettuce", "cheese"]
        return Burger(ingredients)

    def createVeganBurger(self):
        ingredients = ["bun", "special-sauce", "veggie-patty"]
        return Burger(ingredients)


burgerFactory = BurgerFactory()
burgerFactory.createVeganBurger().print()
burgerFactory.createCheeseBurger().print()
burgerFactory.createDulexChesseBurger().print()

