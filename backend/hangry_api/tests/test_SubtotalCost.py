from api.controllers import Subtotal
from types import SimpleNamespace

def test_SimpleCost():
  #Arrange
  order = [
    SimpleNamespace(quantity=5, item=SimpleNamespace(price=1.0)),
    SimpleNamespace(quantity=5, item=SimpleNamespace(price=1.0)),
    SimpleNamespace(quantity=5, item=SimpleNamespace(price=1.0)),
  ]
  #Act
  cost = Subtotal.calculate(order)
  #Assert
  assert cost == 15


def test_ComplexCost():
  #Arrange
  order = [
    SimpleNamespace(quantity=2, item=SimpleNamespace(price=3.5)),
    SimpleNamespace(quantity=1, item=SimpleNamespace(price=4.5)),
  ]
  #Act
  cost = Subtotal.calculate(order)
  #Assert
  assert cost == 11.5
