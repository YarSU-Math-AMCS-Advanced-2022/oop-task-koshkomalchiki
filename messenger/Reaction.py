from abc import ABC


# Абстрактный класс; Интерфейс
class Reaction(ABC):
    def get_name(self) -> str:
        pass

    def get_amount(self) -> int:
        pass

    def __set_name(self, name: str):
        pass

    def __set_amount(self, value: int):
        pass

    def _update_amount(self, value: int):
        pass


# Рекция - "Нравится"
class Like(Reaction):
    amount: int
    name: str

    def __init__(self, amount: int = 0):
        self.amount = amount
        self.name = 'Нравится'

    def get_name(self) -> str:
        return self.name

    def get_amount(self) -> int:
        return self.amount

    def __set_name(self, name: str):
        self.name = name

    def __set_amount(self, amount: int):
        self.amount = amount

    def _update_amount(self, value: int):
        self.amount = max(0, self.amount + value)


# Рекция - "Смешно"
class Funny(Reaction):
    amount: int
    name: str

    def __init__(self, amount: int = 0):
        self.amount = amount
        self.name = 'Смешно'

    def get_name(self) -> str:
        return self.name

    def get_amount(self) -> int:
        return self.amount

    def __set_name(self, name: str):
        self.name = name

    def __set_amount(self, amount: int):
        self.amount = amount

    def _update_amount(self, value: int):
        self.amount = max(0, self.amount + value)


# Рекция - "Ого!"
class Wow(Reaction):
    amount: int
    name: str

    def __init__(self, amount: int = 0):
        self.amount = amount
        self.name = 'Ого!'

    def get_name(self) -> str:
        return self.name

    def get_amount(self) -> int:
        return self.amount

    def __set_name(self, name: str):
        self.name = name

    def __set_amount(self, amount: int):
        self.amount = amount

    def _update_amount(self, value: int):
        self.amount = max(0, self.amount + value)


# Рекция - "Восторг"
class Delight(Reaction):
    amount: int
    name: str

    def __init__(self, amount: int = 0):
        self.amount = amount
        self.name = 'Восторг'

    def get_name(self) -> str:
        return self.name

    def get_amount(self) -> int:
        return self.amount

    def __set_name(self, name: str):
        self.name = name

    def __set_amount(self, amount: int):
        self.amount = amount

    def _update_amount(self, value: int):
        self.amount = max(0, self.amount + value)


# Рекция - "Печаль"
class Sadness(Reaction):
    amount: int
    name: str

    def __init__(self, amount: int = 0):
        self.amount = amount
        self.name = 'Печаль'

    def get_name(self) -> str:
        return self.name

    def get_amount(self) -> int:
        return self.amount

    def __set_name(self, name: str):
        self.name = name

    def __set_amount(self, amount: int):
        self.amount = amount

    def _update_amount(self, value: int):
        self.amount = max(0, self.amount + value)


# Рекция - "!@#$%"; "Недовольство"
class Outrage(Reaction):
    amount: int
    name: str

    def __init__(self, amount: int = 0):
        self.amount = amount
        self.name = '!@#$%'

    def get_name(self) -> str:
        return self.name

    def get_amount(self) -> int:
        return self.amount

    def __set_name(self, name: str):
        self.name = name

    def __set_amount(self, amount: int):
        self.amount = amount

    def _update_amount(self, value: int):
        self.amount = max(0, self.amount + value)
