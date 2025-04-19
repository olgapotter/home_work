def task_1() -> None:

    number_int = 10            # int
    number_float = 3.14        # float
    text = "Привет!"           # str
    items = [1, 2, 3]          # list
    is_valid = True            # bool

    print("Тип number_int:", type(number_int))
    print("Тип number_float:", type(number_float))
    print("Тип text:", type(text))
    print("Тип items:", type(items))
    print("Тип is_valid:", type(is_valid))

task_1()


def task_2() -> None:
    a = [1, 2, 3, 5, 8, 13, 21]

    print("Первые 3 значения списка:", a[:3])

task_2()


def task_3(number: int) -> int:
    return number ** 2

print(task_3(5))