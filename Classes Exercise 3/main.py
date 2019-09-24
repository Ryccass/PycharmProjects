class Lunch:

    def __init__(self,menu):
        self.menu = menu

    def menuPrice(self):
        if self.menu == 'menu 1':
            return f'Your choice {self.menu} \nPrice 12.00'
        elif self.menu == 'menu 2':
            return f'Your choice {self.menu} \nPrice 13.40'
        else:
            return f'Your choice {self.menu} \n Error in Menu'

new = Lunch("menu 1")
print(new.menuPrice())