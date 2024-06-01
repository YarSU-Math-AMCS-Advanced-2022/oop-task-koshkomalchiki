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
    # Количество данной реакции
    amount: int
    # Название данной реакции для интерфейса
    name: str

    # Проверяет является ли число целым не отрицательным
    @staticmethod
    def _is_non_negative_int(value: int) -> bool:
        if not isinstance(value, int):
            raise TypeError(
                "'_is_non_negative_int' - expected a value of type int."
            )
        if value < 0:
            raise ValueError(
                "'_is_non_negative_int' - the amount can not be negative."
            )
        return True

    def __init__(self, amount: int = 0):
        if self._is_non_negative_int(amount):
            self.amount = amount

        self.name = 'Нравится'

    # Возвращеет название данного класса для интерфейска
    def get_name(self) -> str:
        return self.name

    # Возвращает общее количество реакций данного экземпляра
    def get_amount(self) -> int:
        return self.amount

    # Устанавливает название данного класса для интерфейса
    def __set_name(self, name: str):
        if not isinstance(name, str):
            raise TypeError("'__set_name' - expected a value of type str.")

        self.name = name

    # Устанавливает общее количество реакций данного эеземпляра
    def __set_amount(self, amount: int):
        if self._is_non_negative_int(amount):
            self.amount = amount

    # Изменяет общее количество реакций данного экземпляра
    def _update_amount(self, value: int):
        if not isinstance(value, int):
            raise TypeError(
                "'_update_amount' - expected a value of type int."
            )
        if self.amount < -value:
            raise ValueError(
                "'_update_amount' - the amount can not be negative."
            )

        self.amount += value

    # Соответствует действию "поставить данную реакцию"
    def _plus_one_reaction(self):
        self._update_amount(1)

    # Соответствует действию "убрать данную реакцию"
    def _minus_one_reaction(self):
        # Хеширование. Отслеживается наличием реакции от человека
        if self.amount - 1 >= 0:
            self._update_amount(-1)


# Рекция - "Смешно"
class Funny(Reaction):
    # Количество данной реакции
    amount: int
    # Название данной реакции для интерфейсаamount: int
    name: str

    # Проверяет является ли число целым не отрицательным
    @staticmethod
    def _is_non_negative_int(value: int) -> bool:
        if not isinstance(value, int):
            raise TypeError(
                "'_is_non_negative_int' - expected a value of type int."
            )
        if value < 0:
            raise ValueError(
                "'_is_non_negative_int' - the amount can not be negative."
            )
        return True

    def __init__(self, amount: int = 0):
        if self._is_non_negative_int(amount):
            self.amount = amount

        self.name = 'Смешно'

    # Возвращеет название данного класса для интерфейска
    def get_name(self) -> str:
        return self.name

    # Возвращает общее количество реакций данного экземпляра
    def get_amount(self) -> int:
        return self.amount

    # Устанавливает название данного класса для интерфейса
    def __set_name(self, name: str):
        if not isinstance(name, str):
            raise TypeError("'__set_name' - expected a value of type str.")

        self.name = name

    # Устанавливает общее количество реакций данного эеземпляра
    def __set_amount(self, amount: int):
        if self._is_non_negative_int(amount):
            self.amount = amount

    # Изменяет общее количество реакций данного экземпляра
    def _update_amount(self, value: int):
        if not isinstance(value, int):
            raise TypeError(
                "'_update_amount' - expected a value of type int."
            )
        if self.amount < -value:
            raise ValueError(
                "'_update_amount' - the amount can not be negative."
            )

        self.amount += value

    # Соответствует действию "поставить данную реакцию"
    def _plus_one_reaction(self):
        self._update_amount(1)

    # Соответствует действию "убрать данную реакцию"
    def _minus_one_reaction(self):
        # Хеширование. Отслеживается наличием реакции от человека
        if self.amount - 1 >= 0:
            self._update_amount(-1)


# Рекция - "Ого!"
class Wow(Reaction):
    # Количество данной реакции
    amount: int
    # Название данной реакции для интерфейсаamount: int
    name: str

    # Проверяет является ли число целым не отрицательным
    @staticmethod
    def _is_non_negative_int(value: int) -> bool:
        if not isinstance(value, int):
            raise TypeError(
                "'_is_non_negative_int' - expected a value of type int."
            )
        if value < 0:
            raise ValueError(
                "'_is_non_negative_int' - the amount can not be negative."
            )
        return True

    def __init__(self, amount: int = 0):
        if self._is_non_negative_int(amount):
            self.amount = amount

        self.name = 'Ого!'

    # Возвращеет название данного класса для интерфейска
    def get_name(self) -> str:
        return self.name

    # Возвращает общее количество реакций данного экземпляра
    def get_amount(self) -> int:
        return self.amount

    # Устанавливает название данного класса для интерфейса
    def __set_name(self, name: str):
        if not isinstance(name, str):
            raise TypeError("'__set_name' - expected a value of type str.")

        self.name = name

    # Устанавливает общее количество реакций данного эеземпляра
    def __set_amount(self, amount: int):
        if self._is_non_negative_int(amount):
            self.amount = amount

    # Изменяет общее количество реакций данного экземпляра
    def _update_amount(self, value: int):
        if not isinstance(value, int):
            raise TypeError(
                "'_update_amount' - expected a value of type int."
            )
        if self.amount < -value:
            raise ValueError(
                "'_update_amount' - the amount can not be negative."
            )

        self.amount += value

    # Соответствует действию "поставить данную реакцию"
    def _plus_one_reaction(self):
        self._update_amount(1)

    # Соответствует действию "убрать данную реакцию"
    def _minus_one_reaction(self):
        # Хеширование. Отслеживается наличием реакции от человека
        if self.amount - 1 >= 0:
            self._update_amount(-1)


# Рекция - "Восторг"
class Delight(Reaction):
    # Количество данной реакции
    amount: int
    # Название данной реакции для интерфейсаamount: int
    name: str

    # Проверяет является ли число целым не отрицательным
    @staticmethod
    def _is_non_negative_int(value: int) -> bool:
        if not isinstance(value, int):
            raise TypeError(
                "'_is_non_negative_int' - expected a value of type int."
            )
        if value < 0:
            raise ValueError(
                "'_is_non_negative_int' - the amount can not be negative."
            )
        return True

    def __init__(self, amount: int = 0):
        if self._is_non_negative_int(amount):
            self.amount = amount

        self.name = 'Восторг'

    # Возвращеет название данного класса для интерфейска
    def get_name(self) -> str:
        return self.name

    # Возвращает общее количество реакций данного экземпляра
    def get_amount(self) -> int:
        return self.amount

    # Устанавливает название данного класса для интерфейса
    def __set_name(self, name: str):
        if not isinstance(name, str):
            raise TypeError("'__set_name' - expected a value of type str.")

        self.name = name

    # Устанавливает общее количество реакций данного эеземпляра
    def __set_amount(self, amount: int):
        if self._is_non_negative_int(amount):
            self.amount = amount

    # Изменяет общее количество реакций данного экземпляра
    def _update_amount(self, value: int):
        if not isinstance(value, int):
            raise TypeError(
                "'_update_amount' - expected a value of type int."
            )
        if self.amount < -value:
            raise ValueError(
                "'_update_amount' - the amount can not be negative."
            )

        self.amount += value

    # Соответствует действию "поставить данную реакцию"
    def _plus_one_reaction(self):
        self._update_amount(1)

    # Соответствует действию "убрать данную реакцию"
    def _minus_one_reaction(self):
        # Хеширование. Отслеживается наличием реакции от человека
        if self.amount - 1 >= 0:
            self._update_amount(-1)


# Рекция - "Печаль"
class Sadness(Reaction):
    # Количество данной реакции
    amount: int
    # Название данной реакции для интерфейсаamount: int
    name: str

    # Проверяет является ли число целым не отрицательным
    @staticmethod
    def _is_non_negative_int(value: int) -> bool:
        if not isinstance(value, int):
            raise TypeError(
                "'_is_non_negative_int' - expected a value of type int."
            )
        if value < 0:
            raise ValueError(
                "'_is_non_negative_int' - the amount can not be negative."
            )
        return True

    def __init__(self, amount: int = 0):
        if self._is_non_negative_int(amount):
            self.amount = amount

        self.name = 'Печаль'

    # Возвращеет название данного класса для интерфейска
    def get_name(self) -> str:
        return self.name

    # Возвращает общее количество реакций данного экземпляра
    def get_amount(self) -> int:
        return self.amount

    # Устанавливает название данного класса для интерфейса
    def __set_name(self, name: str):
        if not isinstance(name, str):
            raise TypeError("'__set_name' - expected a value of type str.")

        self.name = name

    # Устанавливает общее количество реакций данного эеземпляра
    def __set_amount(self, amount: int):
        if self._is_non_negative_int(amount):
            self.amount = amount

    # Изменяет общее количество реакций данного экземпляра
    def _update_amount(self, value: int):
        if not isinstance(value, int):
            raise TypeError(
                "'_update_amount' - expected a value of type int."
            )
        if self.amount < -value:
            raise ValueError(
                "'_update_amount' - the amount can not be negative."
            )

        self.amount += value

    # Соответствует действию "поставить данную реакцию"
    def _plus_one_reaction(self):
        self._update_amount(1)

    # Соответствует действию "убрать данную реакцию"
    def _minus_one_reaction(self):
        # Хеширование. Отслеживается наличием реакции от человека
        if self.amount - 1 >= 0:
            self._update_amount(-1)


# Рекция - "!@#$%"; "Недовольство"
class Outrage(Reaction):
    # Количество данной реакции
    amount: int
    # Название данной реакции для интерфейсаamount: int
    name: str

    # Проверяет является ли число целым не отрицательным
    @staticmethod
    def _is_non_negative_int(value: int) -> bool:
        if not isinstance(value, int):
            raise TypeError(
                "'_is_non_negative_int' - expected a value of type int."
            )
        if value < 0:
            raise ValueError(
                "'_is_non_negative_int' - the amount can not be negative."
            )
        return True

    def __init__(self, amount: int = 0):
        if self._is_non_negative_int(amount):
            self.amount = amount

        self.name = '!@#$%'

    # Возвращеет название данного класса для интерфейска
    def get_name(self) -> str:
        return self.name

    # Возвращает общее количество реакций данного экземпляра
    def get_amount(self) -> int:
        return self.amount

    # Устанавливает название данного класса для интерфейса
    def __set_name(self, name: str):
        if not isinstance(name, str):
            raise TypeError("'__set_name' - expected a value of type str.")

        self.name = name

    # Устанавливает общее количество реакций данного эеземпляра
    def __set_amount(self, amount: int):
        if self._is_non_negative_int(amount):
            self.amount = amount

    # Изменяет общее количество реакций данного экземпляра
    def _update_amount(self, value: int):
        if not isinstance(value, int):
            raise TypeError(
                "'_update_amount' - expected a value of type int."
            )
        if self.amount < -value:
            raise ValueError(
                "'_update_amount' - the amount can not be negative."
            )

        self.amount += value

    # Соответствует действию "поставить данную реакцию"
    def _plus_one_reaction(self):
        self._update_amount(1)

    # Соответствует действию "убрать данную реакцию"
    def _minus_one_reaction(self):
        # Хеширование. Отслеживается наличием реакции от человека
        if self.amount - 1 >= 0:
            self._update_amount(-1)
