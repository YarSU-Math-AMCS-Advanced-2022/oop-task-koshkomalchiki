class profile:
    def __init__(self, username, usersurname, usermiddlename=''):
        self.name = username
        self.username = usersurname
        self.usermiddlename=usermiddlename
    friends_list = []
    active_new_list=[]
    active_messengers = dict()
    new_messengers = 0
    new_visitors = 0
    def get_information_about_profile(self):
        print("Full name", end=': ')
        print(self.name, end=' ')
        print(self.username, end=' ')
        print(self.usermiddlename, end=' ')
    def get_name(self):
        return self.name
    def get_new_messengers(self):
        to_r = profile.new_messengers
        profile.new_messengers=0
        return to_r
    def get_new_visiotrs(self):
        to_r = profile.new_visitors
        profile.new_visitors=0
        return to_r
    def show_news(self):
        for c in profile.active_new_list:
            print(c)
        profile.active_new_list.clear()

globaly_data_base = dict()
globaly_access = dict()
Now_in_some_account=False
def add_account():
    print("Введите имя нового пользователя")
    name = input()
    print("Введите фамилию нового пользователя")
    surname=input()
    print("Введите отчество нового пользователя")
    middlename=input()
    print("Введите логин")
    login=input()
    print("Введите пароль")
    password=input()
    print("Новый пользователь создан")
    New_Account = profile(name, surname, middlename)
    globaly_access[login]=password
    globaly_data_base[login]=New_Account
    return
def Account_Functions(login):
    print("Рады видеть вас снова в сети")
    profile = globaly_data_base[login]
    print("У вас целых",end=' ')
    print(profile.get_new_messengers(), end=' ')
    print("новых сообщений")
    print("За последние несколько часов вашу страницу посетили", end=' ')
    print(profile.get_new_visiotrs(), end=' ')
    print("человек")
    print("1. Мой профиль")
    print("2. Новостная лента")
    print("3. Сообщения")
    print("4. Друзья")
    print("5. Группы")
    print("6. Музыка")
    print("7. Выйти")
    type=input()
    if(type==1):
        profile.get_information_about_profile()
        print("Список друзей:")
        for g in profile.friends_list:
            print(g.get_infomration_about_profile)
    if (type==2):
        profile.show_news()
    if(type==3):
        print("Функция в разработке")
    if(type==4):
        print("Функция в разработке")
    if(type==5):
        print("Функция в разработке")
    if(type==6):
        print("Фнукция в разработке")
    if(type==7):
        print("Ждем назад, до свидания")
def welcome_function():
    while True:
        print("Добро пожаловать в социальную сеть вконтакте")
        print("Доступные функции для пользователя:")
        print("1. Создать аккаунт")
        print("2. Войти в уже существующий аккаунт")
        type=int(input())
        if (type==1):
            add_account()
        else:
            print("Введите логин и пробель через enter")
            try_login = input()
            if (try_login in globaly_access):
                Now_in_some_account = True
                password = input()
                if (globaly_access[try_login] == password):
                    Account_Functions(try_login)
                else:
                    print("Неверный логин или пароль")
            else:
                print("Неверный логин или пароль")

first_profile = profile("nikita", "artur", "pavlovich")
welcome_function()
# class funcs_user_page:
#     """Реализация функций страницы пользователя"""
#
#     def __init__(self, new_name, new_surname, new_middle_name):
#         """Личная информация пользователя."""
#         self.name = ""
#         self.name = new_name
#         self.surname = ""
#         self.surname = new_surname
#         self.middle_name = ""
#         self.middle_name = new_middle_name
#
#         self.date_birth = [0, 0, 0]
#
#         self.place_birth = ""
#         self.telephone = ""
#         self.place_study = ""
#
#         self.favorite_films = []
#         self.favorite_music = []
#         self.favorite_books = []
#
#         """Информация o странице пользователя."""
#         self.friends = []
#         self.posts = []
#         self.subscribers = []
#
#     """Имя"""
#
#     def get_name(self):
#         if self.name != "":
#             return self.name
#         else:
#             # Если пользователь удалит имя
#             return "Имя не указано"
#
#     def delete_name(self):
#         self.name = ""
#
#     def change_name(self, new_name):
#         self.name = new_name
#
#     """Фамилия"""
#
#     def get_surname(self):
#         if self.surname != "":
#             return self.surname
#         else:
#             return "Фамилия не указана"
#
#     def delete_surname(self):
#         self.surname = ""
#
#     def change_surname(self, new_surname):
#         self.surname = new_surname
#
#     """Отчество"""
#
#     def get_middle_name(self):
#         if self.middle_name != "":
#             return self.middle_name
#         else:
#             return "Отчество не указано"
#
#     def delete_middle_name(self):
#         self.middle_name = ""
#
#     def change_middle_name(self, new_middle_name):
#         self.middle_name = new_middle_name
#
#     """Дата рождения"""
#
#     def get_date_birth(self):
#         return self.date_birth
#
#     def delete_date_birth(self):
#         for i in range(3):
#             self.date_birth[i] = 0
#
#     def change_date_birth(self, new_date_birth):
#         self.date_birth = copy.copy(new_date_birth)
#
#     def print_date_birth(self):
#         if self.date_birth[0] != 0:
#             print(self.date_birth[0], ".",
#                   self.date_birth[1], ".",
#                   self.date_birth[2],
#                   sep=''
#                   )
#         else:
#             print("Дата рождения не указана.")
#
#     """Место рождения"""
#
#     def get_place_birth(self):
#         if self.place_birth != "":
#             return self.place_birth
#         else:
#             return "Метсто рождения не указано"
#
#     def change_place_birth(self, new_place_birth):
#         self.place_birth = new_place_birth
#
#     def delete_place_birth(self):
#         self.place_birth = ''
#
#     """Телефон"""
#
#     def get_telephone(self):
#         if self.telephone != "":
#             return self.telephone
#         else:
#             return "Телефон не указан"
#
#     def change_telephone(self, new_telephone):
#         self.telephone = new_telephone
#
#     def delete_telephone(self):
#         self.telephone = ''
#
#     """Место учёбы"""
#
#     def get_place_study(self):
#         if self.place_study != "":
#             return self.place_study
#         else:
#             return "Место учебы не указано"
#
#     def change_place_study(self, new_place_study):
#         self.place_study = new_place_study
#
#     def delete_place_study(self):
#         self.place_study = ''
#
#     """Фильмы"""
#
#     def add_film(self, new_film):
#         self.favorite_films.append(new_film)
#
#     def get_num_films(self):
#         return len(self.favorite_films)
#
#     def get_films(self):
#         return self.favorite_films
#
#     def print_films(self):
#         if len(self.favorite_films) != 0:
#             for i in range(len(self.favorite_films)):
#                 print(self.favorite_films[i])
#         else:
#             print("Фильмы не указаны.")
#
#     def exclude_film(self, film):
#         self.favorite_films.remove(self.favorite_films.index(film))
#
#     """Музыка"""
#
#     def add_music(self, new_music):
#         self.favorite_music.append(new_music)
#
#     def get_num_music(self):
#         return len(self.favorite_music)
#
#     def get_music(self):
#         return self.favorite_music
#
#     def print_music(self):
#         if len(self.favorite_music) != 0:
#             for i in range(len(self.favorite_music)):
#                 print(self.favorite_music[i])
#         else:
#             print("Музыка не указана.")
#
#     def exclude_music(self, music):
#         self.favorite_music.remove(self.favorite_music.index(music))
#
#     """Книги"""
#
#     def add_books(self, new_books):
#         self.favorite_books.append(new_books)
#
#     def get_num_books(self):
#         return len(self.favorite_books)
#
#     def get_books(self):
#         return self.favorite_books
#
#     def print_books(self):
#         if len(self.favorite_books) != 0:
#             for i in range(len(self.favorite_books)):
#                 print(self.favorite_books[i])
#         else:
#             print("Книги не указаны.")
#
#     def exclude_book(self, book):
#         self.favorite_books.remove(self.favorite_books.index(book))
#
#     # """Информация o странице пользователя."""
#     #       self.friends = []
#     #       self.posts = []
#     #       self.subscribers = []
#     """Друзья"""
#
#     def add_friend(self, new_friend):
#         self.friends.append(new_friend)
#
#     def get_num_friends(self):
#         return len(self.friends)
#
#     def get_friends(self):
#         return self.friends
#
#     def print_friends(self):
#         if len(self.friends) != 0:
#             for i in range(len(self.friends)):
#                 print(self.friends[i])
#         else:
#             print("Друзей нет.")
#
#     def exclude_friend(self, friend):
#         self.friends.remove(self.friends.index(friend))
#
#     """Посты"""
#
#     def add_posts(self, new_post):
#         self.posts.append(new_post)
#
#     def get_num_posts(self):
#         return len(self.posts)
#
#     def get_posts(self):
#         return self.posts
#
#     def print_posts(self):
#         if len(self.posts) != 0:
#             for i in range(len(self.posts)):
#                 print(self.posts[i])
#         else:
#             print("Постов нет.")
#
#     def exclude_post(self, post):
#         self.posts.remove(self.posts.index(post))
#
#     """Подписчики"""
#
#     def add_subscriber(self, new_subscriber):
#         self.subscribers.append(new_subscriber)
#
#     def get_num_subscribers(self):
#         return len(self.subscribers)
#
#     def get_subscribers(self):
#         return self.subscribers
#
#     def print_subscribers(self):
#         if len(self.subscribers) != 0:
#             for i in range(len(self.subscribers)):
#                 print(self.subscribers[i])
#         else:
#             print("Подписчиков нет.")
