class Pizza:
    """Класс для пицц, в него входят основные компоненты готовки"""

    def __init__(self, size='L'):
        self.name = 'Pizza'
        self.size = size
        self.ingredients = {'dough': '200 grams',
                            'tomato sauce': '2 spoons',
                            'mozzarella': '50 grams'}

    def __repr__(self):
        """Выводит название пиццы"""
        return self.name

    def dict(self) -> None:
        """Выводит ингридиенты"""
        print(self.name + ' (' + self.size + '):\n'
              + ''.join(['- ' + x + ' (' + y + ')\n' for x, y in self.ingredients.items()]))

    def __eq__(self, other) -> bool:
        """Сравнение пицц"""
        return (self.ingredients == other.ingredients) and (self.name == other.name)


class Margherita(Pizza):
    """Класс для маргариты"""

    def __init__(self, size='L'):
        super().__init__(size)
        self.name = 'Margherita 🧀'
        self.ingredients = {**self.ingredients,
                            'tomatoes': '5 pieces'}

class Hawaiian(Pizza):
    """Класс для гавайской"""

    def __init__(self, size='L'):
        super().__init__(size)
        self.name = 'Margherita 🍍'
        self.ingredients = {**self.ingredients,
                            'chicken': '10 pieces',
                            'pineapples': '10 pieces'}

class Pepperoni(Pizza):
    """Класс для пепперони"""

    def __init__(self, size='L'):
        super().__init__(size)
        self.name = 'Margherita 🍕'
        self.ingredients = {**self.ingredients,
                            'pepperoni': '10 pieces'}

