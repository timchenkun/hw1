import click
from pizza import Margherita, Hawaiian, Pepperoni
import processing

@click.group()
def cli():
    pass

@cli.command()
@click.argument("name", nargs=1)
@click.argument("size", nargs=1)
@click.option("--delivery", default=False, is_flag=True)
def order(name: str, size: str, delivery: bool) -> None:
    """Готовит и доставляет пиццу."""
    pizza = globals()[name.lower().title()]
    print(processing.bake(pizza(size=size)))
    if delivery:
        print(processing.delivery(pizza(size=size)))
    else:
        print(processing.pickup(pizza(size=size)))

@cli.command()
def menu() -> None:
    """Выводит меню"""

    pizzas = [Margherita(size="L"),
              Margherita(size="XL"),
              Hawaiian(size="L"),
              Hawaiian(size="XL"),
              Pepperoni(size="L"),
              Pepperoni(size="XL")
              ]
    print("🍕 Меню:")
    for pizza in pizzas:
        print('-',pizza, '(' + pizza.size + ') \n', ', '.join(pizza.ingredients.keys()))


if __name__ == "__main__":
    cli()