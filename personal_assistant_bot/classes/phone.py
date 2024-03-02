try:
   from classes.field import Field
except ModuleNotFoundError:
   from personal_assistant_bot.classes.field import Field

from colorama import init, Fore
init(autoreset=True)


class Phone(Field):
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError(Fore.RED + 'Incorrect number format. Please enter a 10-digit number.')
        self.__value = value
