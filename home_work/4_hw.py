class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):

        return self.width * self.height

    def perimeter(self):

        return 2 * (self.width + self.height)


rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)
rect3 = Rectangle(8, 2)

print(f"Прямоугольник 1: Площадь = {rect1.area()}, Периметр = {rect1.perimeter()}")
print(f"Прямоугольник 2: Площадь = {rect2.area()}, Периметр = {rect2.perimeter()}")
print(f"Прямоугольник 3: Площадь = {rect3.area()}, Периметр = {rect3.perimeter()}")



class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        """Сложение a и b"""
        result = self.a + self.b
        print(f"Сложение: {self.a} + {self.b} = {result}")

    def multiplication(self):
        """Умножение a и b"""
        result = self.a * self.b
        print(f"Умножение: {self.a} * {self.b} = {result}")

    def division(self):
        """Деление a на b"""
        if self.b != 0:
            result = self.a / self.b
            print(f"Деление: {self.a} / {self.b} = {result}")
        else:
            print("Ошибка: деление на ноль невозможно.")

    def subtraction(self):
        """Вычитание b из a"""
        result = self.a - self.b
        print(f"Вычитание: {self.a} - {self.b} = {result}")

math_obj = Math(10, 5)

math_obj.addition()
math_obj.multiplication()
math_obj.division()
math_obj.subtraction()


class SidebarButton:
    def __init__(self, text, locator=""):
        self.text = text
        self.type = "Кнопка"
        self.locator = locator

    def click(self):
        return f"Клик по кнопке {self.text}"

# Создание объектов для каждой кнопки 2-го уровня
text_box = SidebarButton("Text Box")
check_box = SidebarButton("Check Box")
radio_button = SidebarButton("Radio Button")
web_tables = SidebarButton("Web Tables")
buttons = SidebarButton("Buttons")
links = SidebarButton("Links")
broken_links_images = SidebarButton("Broken Links - Images")
upload_download = SidebarButton("Upload and Download")
dynamic_properties = SidebarButton("Dynamic Properties")

# Список всех кнопок
buttons_list = [
    text_box, check_box, radio_button, web_tables,
    buttons, links, broken_links_images, upload_download, dynamic_properties
]

# Вывод текста для каждой кнопки
print("Тексты всех кнопок:")
for button in buttons_list:
    print(f"- {button.text}")

# Вызов метода "Клик" для каждой кнопки
print("\nРезультаты кликов:")
for button in buttons_list:
    print(button.click())