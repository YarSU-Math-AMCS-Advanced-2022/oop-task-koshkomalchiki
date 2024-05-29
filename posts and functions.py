from abc import ABC, abstractmethod
from datetime import datetime

# Абстрактный класс для поста
class IPost(ABC):
    # Абстрактное свойство для сообщения поста
    @property
    @abstractmethod
    def msg(self):
        pass

    # Абстрактный метод для установки сообщения поста
    @msg.setter
    @abstractmethod
    def msg(self, value):
        pass

    # Абстрактное свойство для времени публикации поста
    @property
    @abstractmethod
    def time(self):
        pass

    # Абстрактный метод для установки времени публикации поста
    @time.setter
    @abstractmethod
    def time(self, value):

        pass

# Абстрактный класс для пользователя
class IUser(ABC):
    # Абстрактный метод для получения ленты постов
    @abstractmethod
    def get_lenta(self, time):
        pass

    # Абстрактный метод для публикации поста в группу
    @abstractmethod
    def publicate(self, post, group):
        pass

    # Абстрактный метод для создания и добавления поста
    @abstractmethod
    def set_post(self, msg):
        pass

# Конкретная реализация класса Post, наследующего IPost
class Post(IPost):
    def __init__(self):
        # Инициализация объекта Post
        self._msg = ""  # Изначально сообщение пустое
        self._time = datetime.now()  # Установка текущего времени как время создания поста

    # Геттер для свойства msg
    @property
    def msg(self):
        return self._msg

    # Сеттер для свойства msg
    @msg.setter
    def msg(self, value):
        self._msg = value

    # Геттер для свойства time
    @property
    def time(self):
        return self._time

    # Сеттер для свойства time
    @time.setter
    def time(self, value):
        self._time = value

# Конкретная реализация класса User, наследующего IUser
class User(IUser):
    def __init__(self, name="Unknown"):
        # Инициализация объекта User
        self.name = name  # Установка имени пользователя
        self._lenta = []  # Изначально лента постов пуста
        self._last_call = datetime.now()  # Установка текущего времени как время последнего вызова метода get_lenta
    # Метод для получения ленты постов, опубликованных после последнего вызова метода
    def get_lenta(self, time):
        posts = [post for post in self._lenta if post.time > self._last_call]  # Фильтрация постов по времени
        self._last_call = datetime.now()  # Обновление времени последнего вызова метода
        return '\n'.join([post.msg for post in posts])  # Возврат сообщений постов в виде строки
    # Метод для публикации поста в группу
    def publicate(self, post, group):
        group.publicate(post)  # Вызов метода публикации в группе
    # Метод для создания и добавления поста в ленту
    def set_post(self, msg):
        post = Post()  # Создание нового поста
        post.msg = msg  # Установка сообщения поста
        self._lenta.append(post)  # Добавление поста в ленту

# Пример использования классов
if __name__ == "__main__":
    # Примерная реализация класса Group для демонстрации метода publicate
    class Group:
        def publicate(self, post):
            # Метод для публикации поста в группу
            print(f"Group: {post}")  # Печать сообщения поста

    # Создание пользователя и добавление постов в его ленту
    user = User("Alice")  # Создание пользователя с именем Alice
    user.set_post("Hello, world!")  # Добавление первого поста
    user.set_post("This is my second post.")  # Добавление второго поста

    # Вывод ленты пользователя
    print("Lenta:")
    print(user.get_lenta(datetime.now()))  # Печать ленты постов

    # Создание группы и публикация поста в группу
    group = Group()  # Создание объекта Group
    user.publicate("New post in the group!", group)  # Публикация поста в группе
