
# Static methods are similar to class methods, except they don't receive any additional arguments(cls ,self);
# they are identical to normal functions that belong to a class.
#They are marked with the staticmethod decorator.

# Static methods behave like plain functions, except for the fact that you can call them from an instance of the class.

class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings

  @staticmethod
  def validate_topping(topping):
    if topping == "pineapple":
      raise ValueError("No pineapples!")
    else:
      return True

ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
  pizza = Pizza(ingredients)