from Checkers import Checkers
from OptionsMenu import OptionsMenu
from Post import Post
from Reactions import Reactions


class Wall:
    #количество постов
    amount: int
    #список постов в хронологическом порядке
    wall: list[Post, ]
    #имя класса для интерфейса
    title: str

    def __init__(
            self,
            wall: list[Post, ] = [],
            title: str = 'Стена'
    ):
        self._set_wall(wall)
        self._set_title(title)

    #список постов
    def _set_wall(self, wall: list[Post, ]):
        function_name = 'Wall._set_wall()'
        Checkers.type_comparison(
            value=wall,
            type_name=list,
            function_name=function_name
        )
        for post in wall:
            Checkers.type_comparison(
                value=post,
                type_name=Post,
                function_name=function_name
            )
        self.wall = wall
        self.amount = len(wall)

    #новое наименование класса для пользовательского интерфейса
    def _set_title(self, title: str):
        Checkers.type_comparison(
            value=title,
            type_name=str,
            function_name='Wall._set_title()'
        )
        self.title = title

    #возвращаем количество опубликованных постов
    def get_amount(self) -> int:
        return self.amount

    #возвращаем функции для пользовательского интерфейсе
    def get_title(self) -> str:
        return self.title

    #реакция на прочитанный пост
    def _react(self, index: int):
        function_name = 'Wall._react()'
        Checkers.type_comparison(
            value=index,
            type_name=int,
            function_name=function_name
        )

        print('* Введите номер поста, чтобы продолжить')
        print("* Введите знак '..' без скобочек, чтобы вернуться к профилю")
        number_selected_post = input('-> ')
        if not number_selected_post.isdigit():
            print('Введено не корректное значение. Повторите попытку.')
            self._react(index)
        number_selected_post = int(number_selected_post)
        if not Reactions.num_in_range(1, int(number_selected_post), index):
            print(f'Поста с номером {number_selected_post} ' +
                  'не существует или он не прочитан. Повторите попытку')
            self._react(index)

        (
            self
            .wall[number_selected_post - 1]
            .reactions
            .interact()
        )

    #комментируем прочитанный пост
    def _comment(self, index: int):
        function_name = 'Wall._comment()'
        Checkers.type_comparison(
            value=index,
            type_name=int,
            function_name=function_name
        )

        print('* Введите номер поста, чтобы продолжить')
        print("* Введите знак '..' без скобочек, чтобы вернуться к профилю")
        number_selected_post = input('-> ')
        if not number_selected_post.isdigit():
            print('Введено не корректное значение. Повторите попытку.')
            self._comment(index)
        number_selected_post = int(number_selected_post)
        if not Reactions.num_in_range(1, int(number_selected_post), index):
            print(f'Поста с номером {number_selected_post} ' +
                  'не существует или он не прочитан. Повторите попытку')
            self._comment(index)

        (
            self
            .wall[number_selected_post - 1]
            .comments
            .interact()
        )

    #выводим пост по заданному индексу
    def _read_post(self, index: int):
        Checkers.type_comparison(
            value=index,
            type_name=int,
            function_name='Wall._read_post()'
        )
        if not Reactions.num_in_range(0, len(self.wall) - 1, index):
            raise ValueError("'Wall._read_post()' - out of range.")

        filling_number = 75
        prepost = f'Пост ( {index + 1} )'
        print(prepost, '~' * (filling_number - len(prepost) - 1))
        print(f'  {self.wall[index].get_author_name()}')
        print(self.wall[index].get_post())
        print(' ',
              self
              .wall[index]
              .get_date_time()
              .strftime("%Y.%m.%d %H:%M"))
        print('~' * filling_number)

    #добавляем в конец общего списка пост
    def add_post(self, post: Post):
        Checkers.type_comparison(
            value=post,
            type_name=Post,
            function_name='Wall.add_post()'
        )
        self.wall.append(post)
        self.amount += 1

    #создаем и добавляем пост
    def create_and_add_post(self):
        post = Post()
        if post.create():
            self.add_post(post)

    #выводим посты в обратном хронологическом порядке
    def _read_wall(self):
        if not self.amount:
            print('\n( Посты отсутствуют )')
            match OptionsMenu.create(
                menu={
                    '1': 'Написать пост',
                    '..': 'Назад'
                },
                messege='Выберите действие:'
            ):
                case '1':
                    self.create_and_add_post()
                case '..':
                    return

        print('\nТекущее количество постов:', self.get_amount())
        index_current_post = 0
        read_wall = True
        while read_wall:
            for _ in range(3):
                read_wall = index_current_post < self.get_amount()
                if read_wall:
                    print()
                    self._read_post(index_current_post)
                    index_current_post += 1
                else:
                    print('\n( Прочитаны все посты )\n')
                    break

            menu = {
                '': ' Продолжить просмотр ленты',
                '1': 'Отреагировать на прочитанный пост',
                '2': 'Прокомментировать прочитанный пост',
                '3': 'Написать пост',
                '..': 'Назад'
            }
            if not read_wall:
                menu.pop('')
                read_wall = True
            messege = 'Выберите действие:'
            match OptionsMenu.create(menu=menu, messege=messege):
                case '1':   #реагируем на пост
                    self._react(index_current_post)
                case '2':   #комментируем пост
                    self._comment(index_current_post)
                case '3':   #пишем пост
                    self.create_and_add_post()
                case '..':   #возвращаемся к профилю
                    break

    #взаимодействуем с реакциями через консольный интерфейст
    def interact(self):
        self._read_wall()
