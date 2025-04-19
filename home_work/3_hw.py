def task_2(a: float, b: float) -> None:
    print("Наибольшее число:", max(a, b))

task_2(10, 25)


def task_3(a: int, b: int) -> None:
    if abs(a - b) == 135:
        print("yes")
    else:
        print("no")

task_3(270, 135)


def task_4(month: int) -> None:
    if month in [12, 1, 2]:
        print("зима")
    elif month in [3, 4, 5]:
        print("весна")
    elif month in [6, 7, 8]:
        print("лето")
    elif month in [9, 10, 11]:
        print("осень")
    else:
        print("Некорректный номер месяца")

task_4(4)


def task_5(a: int, b: int, c: int) -> None:
    if a > 10 and b > 10 and c > 10:
        print("yes")
    else:
        print("no")

task_5(11, 15, 13)