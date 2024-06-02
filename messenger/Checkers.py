from typing import Any


class Checkers:
    # Проверяет соответствие переменной типу данных
    @staticmethod
    def type_comparison(
        value: Any,
        type_name: type,
        function_name: str
    ):
        if not isinstance(type_name, type):
            raise TypeError("'Checkers.type_comparison' - expected " +
                            "a value of type type.")
        if not isinstance(function_name, str):
            raise TypeError("'Checkers.type_comparison' - expected " +
                            "a value of type str.")
        if not isinstance(value, type_name):
            raise TypeError(f"'{function_name}' - expected a " +
                            f"value of type {type_name}.")
