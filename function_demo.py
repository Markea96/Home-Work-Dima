menu = {
    'Cesar': 200,
    'Soup': 300,
    'Vegetables': 150,
}


def print_menu(demo_menu) -> None:
    for name, price in demo_menu.items():
        print(f'{name} - {price}')


def solve(a: float, b: float, c: float) -> (float, float):
    def get_discriminant(_a, _b, _c) -> float:
        return _b ** 2 - 4 * _a * _c

    discriminant = get_discriminant(a, b, c)

    if discriminant < 0:
        pass
    elif discriminant > 0:
        pass
    else:
        pass


if __name__ == '__main__':
    solve(1, 2, 3)
