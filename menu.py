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
    menu_target[name] = price
    return True


print_demo_menu(menu)
add_menu_item(menu, 'Bread', 100)
print_demo_menu(menu)

"""
1) Check in function add_menu_item that item doesnt exist/ Return False if does 
2) Add function get_new_product() that ask user to input name and price of a new Product and returns a Pair ( name, price )
"""
