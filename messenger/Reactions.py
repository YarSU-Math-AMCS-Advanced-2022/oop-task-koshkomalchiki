import Reaction


# Создаём псевдоним
ReactionsList = list[Reaction.Reaction, ]


class Reactions:
    # Массив всех реакций
    reactions: ReactionsList
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

    def __set_reactions(self, reactions: ReactionsList):
        self._is_ReactionsList(reactions)

        self.reactions = reactions

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
        self.__set_reactions(reactions)
        self.title = 'Реакции'

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

    def __set_title(self, title: str):
        if not isinstance(title, str):
            raise TypeError("'__set_title' - expected a value of type str.")

        self.title = title

    @staticmethod
    def __num_in_range() -> bool:
        pass

    def __select_change_reaction(self, index: int):
        print(' Выберите действие:')
        print(f'   [ 1 ] Поставить {self.reactions[index].get_name()}.')
        print(f'   [ 2 ] Убрать {self.reactions[index].get_name()}.')
        action = input('  -> ')

        match action:
            case '1':
                self.reactions[index]._plus_one_reaction()
            case '2':
                self.reactions[index]._minus_one_reaction()
            case _:
                print('Указан не существующий вариант. Повторите попытку.')
                self.select_change_reaction(index)

    def _select_reaction(self) -> int:
        print('Выберите рекцию:')
        for index, reaction in enumerate(self.reactions):
            print(f'  [ {index + 1} ] {reaction.get_name()}')
        
        reaction_number = input('-> ')
        if any(not reaction_number.isdigit(),
               (reaction_number := int(reaction_number)) < 1,
               len(self.reactions) < reaction_number):
            print('Указан не существующий вариант. Повторите попытку.')
            return self.__select_reaction()

        return reaction_number
