# from typing import Any
import Reaction


# Создаём псевдоним
ReactionsList = list[Reaction.Reaction, ]


class Reactions:
    # Массив всех реакций
    reactions: ReactionsList
    # Максимальная длина названия реакции из списка выше
    # Необходимо для вывода
    __mx_len_reaction_name: int
    # Наименование класса для интерфейса
    title: str

    # Проверяет являются ли элементы массива потомками класса Reaction.Reaction
    @staticmethod
    def _is_ReactionsList(reactions: list[Reaction.Reaction, ]) -> bool:
        for reaction in reactions:
            if not issubclass(type(reaction), Reaction.Reaction):
                print(type(reaction))
                raise TypeError(
                    "'_is_ReactionsList' - expected a value of type kids " +
                    "Reaction."
                )
        return True

    # Вычисляет максимальную длину слов-ключей словаря
    @staticmethod
    def _mx_len_key_word(dictionary) -> int:
        return max([len(word) for word in dictionary.keys()])

    # Задаёт набор реакций
    def _set_reactions(self, reactions: ReactionsList):
        self._is_ReactionsList(reactions)
        self.reactions = reactions
        self.__mx_len_reaction_name = self._mx_len_key_word(
            self.get_reactions()
        )

    def __init__(
            self,
            reactions: ReactionsList = [
                Reaction.Like(),
                Reaction.Funny(),
                Reaction.Wow(),
                Reaction.Delight(),
                Reaction.Sadness(),
                Reaction.Outrage()
            ]
    ):
        self._set_reactions(reactions)
        self.title = 'Реакции'

    # Возвращает наименование класса для пользовательского интерфеса
    def get_title(self) -> str:
        return self.title

    # Возвращает словарь название реакции -> количество реакций
    def get_reactions(self) -> dict[str, int]:
        reactions = dict()
        for reaction in self.reactions:
            reactions[reaction.get_name()] = reaction.get_amount()

        return reactions

    # Добавляет в конец списка новую реакцию
    def _add_reaction(self, reaction: Reaction.Reaction):
        self._is_ReactionsList(list(reaction))
        self.reactions.append(reaction)
        self.__mx_len_reaction_name = max(
            self.__mx_len_reaction_name,
            len(reaction.get_name())
        )

    # Устанавливает новое наименование класса для пользовательского интерфейса
    def __set_title(self, title: str):
        if not isinstance(title, str):
            raise TypeError("'__set_title' - expected a value of type str.")

        self.title = title

    # Проверяет находится ли число в заданном промежутке
    @staticmethod
    def num_in_range(left: int, right: int, value: int) -> bool:
        try:
            return left <= value and value <= right
        except TypeError:
            raise TypeError("'__num_in_range' - expected values of type int")

    # Выводит меню выбора действий над реакцией (поставить/убрать)
    def __select_action_of_reaction(self, index: int):
        if not isinstance(index, int):
            raise TypeError("'__select_action_of_reaction' - expected a " +
                            "value of type int.")
        if not self.num_in_range(0, len(self.reactions) - 1, index):
            raise ValueError("'__select_action_of_reaction' - out of range.")

        print(' Выберите действие:')
        print(f'   [ 1 ] Поставить "{self.reactions[index].get_name()}"')
        print(f'   [ 2 ] Убрать "{self.reactions[index].get_name()}"')
        print('   [ .. ] Назад')
        action = input(' -> ')

        match action:
            case '1':
                self.reactions[index]._plus_one_reaction()
            case '2':
                self.reactions[index]._minus_one_reaction()
            case '..':
                pass
            case _:
                print('Указан не существующий вариант. Повторите попытку.')
                self.__select_action_of_reaction(index)

        print('(Выполнено)')

    # Выводит меню выроба реакции
    def _select_reaction(self) -> int | None:
        print('Выберите рекцию:')
        for index, info in enumerate(self.get_reactions().items()):
            # [!] 8 -> self.__mx_len_reactions_name
            print(f'  [ {index + 1} ] {info[0]:8}\t+{info[1]}')
        print('  [ .. ] Назад')

        reaction_number = input('-> ')

        if reaction_number == '..':
            return None

        if not reaction_number.isdigit() or\
           not self.num_in_range(
               1,
               len(self.reactions),
               int(reaction_number)
           ):
            print('Указан не существующий вариант. Повторите попытку.')
            return self._select_reaction()

        return int(reaction_number) - 1

    # Взаимодействие с реакциями через консольный интерфейст
    def interact_with_reactions(self):
        selected_reaction = self._select_reaction()
        if selected_reaction is not None:
            self.__select_action_of_reaction(selected_reaction)
            self.interact_with_reactions()
