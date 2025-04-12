from typing import Optional

menu = {
    'Cheese': 200,
    'Nuggets': 500,
    'Water': 100,
    'Cola': 200
}


def print_demo_menu(menu_list: dict[str, int]) -> None:
    for name, price in menu_list.items():
        print(f'{name} - {price}')

    print('_' * 50)


def add_menu_item(menu_target: dict[str, int], name: str, price: int) -> bool:
    if menu_target.get(name):
        print('Already exists!')
        return False

    menu_target[name] = price
    return True


def get_new_product():
    _product = input('Enter product name: ')
    _price = input('Enter product price: ')
    return _product, _price


if __name__ == '__main__':
    # print_demo_menu(menu)
    # add_menu_item(menu, 'Bread', 100)
    # add_menu_item(menu, 'Milk', 200)
    # add_menu_item(menu, 'Bread', 100)
    # print_demo_menu(menu)
    product, price = get_new_product()
    print(f'Product name: {product} price: {price}')

"""
1) Write function delete_product ( menu , product_name ) that deletes menu item with product name
2) Write function that solve and print all roots for math equation like: ax**2 + bx + c = 0  
"""


def delete_product(_menu: dict[str, int], product_name: str) -> None:
    if _menu.get(product_name):
        del _menu[product_name]


def solve_square_equation(a: float, b: float, c: float) -> tuple[float | None, float | None]:
    """
    Calculate and return all Roots
    :param a: 
    :param b: 
    :param c: 
    :return: roots as a tuple
    """
    import math

    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root, None
    else:
        return None, None
