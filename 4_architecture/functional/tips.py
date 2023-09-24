from functools import reduce


def decorate(func):
    def inner(*args):
        print("==============================")
        print(f"start {func.__name__}")
        func(*args)
        print(f"end {func.__name__}")

    return inner


@decorate
def multiply_by_2(items: list[int]):
    print(list(map(lambda x: 2 * x, items)))


@decorate
def sum_all(items: list[int]):
    print(reduce(lambda x, y: x + y, items, 0))


@decorate
def get_odd_numbers(items: list[int]):
    print(list(filter(lambda x: x % 2 > 0, items)))


if __name__ == "__main__":
    mylist = [1, 5, 7, 8, 9, 27, 32]
    multiply_by_2(mylist)
    get_odd_numbers(mylist)
    sum_all(mylist)
