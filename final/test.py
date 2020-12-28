import pytest
from pizza import Margherita, Pepperoni, Hawaiian
import processing

def test_eq():
    margherita_1 = Margherita()
    margherita_2 = Margherita()
    hawaiian_1 = Hawaiian()
    hawaiian_2 = Hawaiian()
    pepperoni_1 = Pepperoni()
    pepperoni_2 = Pepperoni()
    assert margherita_1 == margherita_2
    assert hawaiian_1 == hawaiian_2
    assert pepperoni_1 == pepperoni_2
    assert margherita_1 != hawaiian_1
    assert margherita_1 != pepperoni_1
    assert hawaiian_1 != pepperoni_1

def test_name():
    margherita_1 = Margherita()
    hawaiian_1 = Hawaiian()
    pepperoni_1 = Pepperoni()
    assert margherita_1.name == 'Margherita 🧀'
    assert hawaiian_1.name == 'Hawaiian 🍍'
    assert pepperoni_1.name == 'Pepperoni 🍕'

def test_size():
    margherita_1 = Margherita()
    margherita_2 = Margherita('XL')
    assert margherita_1.size == 'L'
    assert margherita_2.size == 'XL'

def test_bake():
    margherita_1 = Margherita()
    assert processing.bake(margherita_1)[:31] == '👨‍🍳 Приготовили Margherita 🧀 за'

def test_delivery():
    margherita_1 = Margherita()
    assert processing.delivery(margherita_1)[:27] == '🛵 Доставили Margherita 🧀 за'

def test_pickup():
    margherita_1 = Margherita()
    assert processing.pickup(margherita_1)[:25] == '💁 Забрали Margherita 🧀 за'
