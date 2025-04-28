class ButtonTwo:

    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc


    def click(self):
        return "Клик по локатору -{}".format(self.loc)


home_two = ButtonTwo('Домой', '/home', 'button#home')

print(home_two.click())
