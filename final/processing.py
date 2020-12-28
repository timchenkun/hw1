import random
from pizza import Pizza
from functools import wraps
from typing import Callable


def log(prints: str) -> Callable:
    """параметрический декоратор"""

    def deco(process: Callable) -> Callable:
        """простой декоратор"""

        @wraps(process)
        def get_str(pizza: Pizza) -> str:
            """Получение начений необходимых для вывода"""

            return prints.format(pizza, random.randint(1, 5))

        return get_str

    return deco


@log("👨‍🍳 Приготовили {} за {} с!")
def bake(pizza: Pizza) -> str:
    """Готовит пиццу"""


@log("🛵 Доставили {} за {} c!")
def delivery(pizza: Pizza) -> str:
    """Доставляет пиццу"""

@log('💁 Забрали {} за {} с!')
def pickup(pizza: Pizza) -> str:
    """Самовывоз"""

