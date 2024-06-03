from datetime import datetime as dt
from Checkers import Checkers
from Comment import Comment
from OptionsMenu import OptionsMenu
from Reactions import Reactions


class Comments:
    # Список всех комментариев в хронологическом порядке
    comments: list[Comment, ]
    # Общее количество комментариев
    amount: int
    # Наименование класса для интерфейса
    title: str

    # Проверяет являются ли элементы массива экземплярами класса Comment
    @staticmethod
    def _is_CommentsList(comments: Comment):
        for comment in comments:
            Checkers.type_comparison(
                value=comment,
                type_name=Comment,
                function_name='Comments._is_commentsList'
            )

    # Задаёт набор реакций
    def __set_comments(self, comments: list[Comment, ]):
        self._is_CommentsList(comments)
        self.comments = comments
        self.amount = len(comments)

    # Устанавливает новое наименование класса для пользовательского интерфейса
    def __set_title(self, title: str):
        Checkers.type_comparison(
            value=title,
            type_name=str,
            function_name='Comments.__set_title()'
        )

        self.title = title

    def __init__(self, comments: list[Comment, ] = []):
        self.__set_comments(comments)
        self.title = 'Комментарии'

    # Возвращает список списков общих данных об оставленных комментария
    def get_comments(self) -> list[list[str, dt, str, dict[str, int]]]:
        return [comment.get_data() for comment in self.comments]

    # Возвращает название функции для пользовательском интерфейсе
    def get_title(self) -> str:
        return self.title

    # Возвращает общее количество оставленных комментариев
    def get_amount(self) -> int:
        return self.amount

    # Добавляет комментарий в конец общего списка комментариев
    def _add_comment(self, comment: Comment):
        Checkers.type_comparison(
            value=comment,
            type_name=Comment,
            function_name='Comments._add_comment()'
        )

        self.comments.append(comment)
        self.amount += 1

    # Создаёт и добавляет комментарий в конец общего списка комментарие
    def add_comment(self):
        comment = Comment()
        if comment.create():
            self._add_comment(comment)

    # Удаляет комментарий по заданному индексу
    def remove_comment(self, index: int):
        Checkers.type_comparison(
            value=index,
            type_name=int,
            function_name='Comments.remove_comment()'
        )
        if index < 1:
            raise ValueError(
                "'remove_comment' - index value must be greater than zero."
            )

        self.comments.remove(index - 1)

    # Выводит комментарий по заданному индексу
    def _read_comment(self, index: int):
        Checkers.type_comparison(
            value=index,
            type_name=int,
            function_name='Comments._read_comment()'
        )
        if not Reactions.num_in_range(0, len(self.comments) - 1, index):
            raise ValueError("'_read_comment' - out of range.")

        filling_number = 75
        precomment = f'Комментарий ( {index + 1} )'
        print(precomment, '-' * (filling_number - len(precomment) - 1))
        print(f'  {self.comments[index].get_author()}')
        print(self.comments[index].get_text())
        print(' ',
              self
              .comments[index]
              .get_datetime()
              .strftime("%Y.%m.%d %H:%M"))
        print('-' * filling_number)

    # [+] Переработать проверку введённого значения
    # Отреагировать на прочитанный комментарий
    def _react(self, index: int):
        function_name = 'Comments._react()'
        Checkers.type_comparison(
            value=index,
            type_name=int,
            function_name=function_name
        )

        number_is_correct = False
        while not number_is_correct:
            print('* Введите номер комментария, чтобы продолжить')
            print("* Введите знак '..' без скобочек, чтобы вернуться к ленте " +
                "комментариев")
            number_selected_comment = input('-> ')
            if number_selected_comment == '..':
                return

            if not number_selected_comment.isdigit():
                print('Введено не корректное значение. Повторите попытку.')
                continue
            number_selected_comment = int(number_selected_comment)
            if number_selected_comment < 1 or index < number_selected_comment:
                print(f'Комментария с номером {number_selected_comment} ' +
                    'не существует или он не прочитан. Повторите попытку')
            else:
                number_is_correct = True

        (
            self
            .comments[number_selected_comment - 1]
            .reactions.interact()
        )

    # [~] Можно сделать в порядре "залайканости"
    # [?] Дублирования ветвления match из Comments.__select_action_of_reading()
    # Выводит комментарии в хронологическом порядке
    def _read_comments(self):
        if not self.amount:
            # match self.__select_action_for_empty_comments():
            print('\n( Комментарии отсутствуют )')
            match OptionsMenu.create(
                menu={
                    '1': 'Написать комментарий',
                    '..': 'Назад'
                },
                messege='Выберите действие:'
            ):
                case '1':
                    self.add_comment()
                case '..':
                    return

        print('\nТекущее количество комментариев:', self.amount)
        # Индекс комментария, который будет выведен
        index_current_comment = 0
        # Продолжить ли прочтение ленты комментариев
        read_comments = True
        while read_comments:
            for _ in range(5):
                read_comments = index_current_comment < self.amount
                if read_comments:
                    print()
                    self._read_comment(index_current_comment)
                    index_current_comment += 1
                else:
                    print('\n( Прочитаны все комментарии )\n')
                    break

            menu = {
                '': ' Продолжить чтение комментариев',
                '1': 'Отреагировать на прочитанный комментарий',
                '2': 'Написать комментарий',
                '..': 'Назад'
            }
            if not read_comments:
                menu.pop('')
                read_comments = True
            messege = 'Выберите действие:'
            match OptionsMenu.create(menu=menu, messege=messege):
                case '1':   # Отреагировать на комментарий
                    self._react(index_current_comment)
                case '2':   # Написать комментарий
                    self.add_comment()
                case '..':   # Вернуться к посту
                    break

    # Взаимодействие с реакциями через консольный интерфейст
    def interact(self):
        self._read_comments()
