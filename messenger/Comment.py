from datetime import datetime as dt
from Checkers import Checkers
from Reactions import Reactions


class Comment:
    # Автор комментария
    author: str
    # Дата и время создания комментария
    date_time: dt
    # Хеш аккаунта автора комментария
    # hesh: str
    # Содержание комментария
    comment: str
    # Реакции поставленные на данный комментарий
    reactions: Reactions

    def __init__(self):
        self.author = 'Павел Дуров'
        self.date_time = dt(2006, 10, 10)
        self.comment = ''
        self.reactions = Reactions()

    # Задаёт автора комментария
    def __set_author(self, author: str):
        Checkers.type_comparison(
            value=author,
            type_name=str,
            function_name='Comment.__set_author()'
        )
        self.author = author

    # Задаёт реакции
    def __set_reactions(self, reactions: Reactions):
        Checkers.type_comparison(
            value=reactions,
            type_name=Reactions,
            function_name='Comment.__set_reactions()'
        )
        self.reactions._set_reactions()

    # Считывает комментарий из консоли пока не встретит на пустой строке <->
    @staticmethod
    def _write_comment() -> str | None:
        break_symbol = '..'
        end_symbol = '<->'

        comment = ''
        new_line = input()
        striped_new_line = new_line.strip()
        while striped_new_line != break_symbol and\
                striped_new_line != end_symbol:
            comment += new_line + '\n'
            new_line = input()
            striped_new_line = new_line.strip()

        return comment[:-1] if striped_new_line != break_symbol else None

    # Создаёт комментарий
    def create(self) -> bool:
        print('\nНапишите комментарий:')
        print("~ Для завершения комментария напишите с " +
              "новой строки знак '<->' без скобочек")
        print("~ Для возвращения к ленте комментариев напишите с " +
              "новой строки знак '..' без скобочек")
        print('<->')

        unchecked_comment = self._write_comment()
        if unchecked_comment is None:
            print('( Черновик удалён )')
            return False
        self.comment = unchecked_comment
        self.date_time = dt.now()
        print('( Комментарий сохранён )')
        return True

    # [~] Стоит заменить на идентификатор, т.е. хеш
    # Возвращает имя и фамилию автора комментария
    def get_author(self) -> str:
        return self.author

    # Возвращает дату и время создания комментария
    def get_datetime(self) -> dt:
        return self.date_time

    # Возвращает текс комментария
    def get_text(self) -> str:
        return self.comment

    # Возвращает общие данные о комментарии
    def get_data(self) -> list[str, dt, str, dict[str, int]]:
        return [self.author, self.date_time, self.comment, ]
