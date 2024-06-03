from datetime import datetime as dt
from Checkers import Checkers
from Comments import Comments
from Reactions import Reactions


class Post:
    author_name: str
    author_hesh: int
    comments: Comments
    date_time: dt
    post: str
    reactions: Reactions
    title: str

    def __init__(
            self,
            author_name: str = 'Павел Дуров',
            author_hesh: int = -1,
            comments: Comments = Comments(),
            date_time: dt = dt(2006, 10, 10),
            post: str = '',
            reactions: Reactions = Reactions(),
            title: str = 'Пост'
    ):
        self._set_author_name(author_name)
        self._set_author_hesh(author_hesh)
        self._set_comments(comments)
        self._set_date_time(date_time)
        self._set_post(post)
        self._set_reactions(reactions)
        self._set_title(title)

    #устанавливаем ФИО автора
    def _set_author_name(self, author_name: str):
        Checkers.type_comparison(
            value=author_name,
            type_name=str,
            function_name='Post._set_author_name()'
        )
        self.author_name = author_name

    #устанавливаем хеш-идентификатор автора
    def _set_author_hesh(self, author_hesh: int):
        Checkers.type_comparison(
            value=author_hesh,
            type_name=int,
            function_name='Post._set_author_name()'
        )
        self.author_hesh = author_hesh

    #устанавливаем комментарии к посту
    def _set_comments(self, comments: Comments):
        Checkers.type_comparison(
            value=comments,
            type_name=Comments,
            function_name='Post._set_comments()'
        )
        self.comments = comments

    #устанавливаем время создания поста
    def _set_date_time(self, date_time: dt):
        Checkers.type_comparison(
            value=date_time,
            type_name=dt,
            function_name='Post._set_date_time()'
        )
        self.date_time = date_time

    #устанавливаем содержание поста
    def _set_post(self, post: str):
        Checkers.type_comparison(
            value=post,
            type_name=str,
            function_name='Post._set_post()'
        )
        self.post = post

    #устанавливаем реакции
    def _set_reactions(self, reactions: Reactions):
        Checkers.type_comparison(
            value=reactions,
            type_name=Reactions,
            function_name='Post._set_reactions()'
        )
        self.reactions = reactions

    #устанавливаем новое наименование класса для пользовательского интерфейса
    def _set_title(self, title: str):
        Checkers.type_comparison(
            value=title,
            type_name=str,
            function_name='Post._set_title()'
        )
        self.title = title

    #возвращаем ФИО автора
    def get_author_name(self) -> str:
        return self.author_name

    #возвращем хеш-идентификатор автора
    def get_author_hesh(self) -> str:
        return self.author_hesh

    #возвращем список списков основной информации комментариев
    def get_comments(self) -> list[list[str, dt, str, dict[str, int]]]:
        return self.comments.get_comments()

    #возвращем дату создания поста
    def get_date_time(self) -> dt:
        return self.date_time

    #возвращаем содержание поста
    def get_post(self) -> str:
        return self.post

    #возвращаем словарь название реакции -> количество реакций
    def get_reactions(self) -> dict[str, int]:
        return self.reactions.get_reactions()

    #возвращаем наименование класса для пользовательского интерфеса
    def get_title(self) -> str:
        return self.title

    #считываем текст поста из консоли пока не встретит на пустой строке <->
    @staticmethod
    def _write_post() -> str | None:
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

    #создаём пост
    def create(self) -> bool:
        print('\n')
        print("~ Для завершения поста напишите с " +
              "новой строки знак '<->' без скобочек")
        print("~ Для возвращения к ленте напишите с " +
              "новой строки знак '..' без скобочек")
        print('<->')

        unchecked_post = self._write_post()
        if unchecked_post is None:
            print('( Черновик удалён )')
            return False
        self._set_post(unchecked_post)
        self._set_date_time(dt.now())
        print('( Пост опубликован )')
        return True
