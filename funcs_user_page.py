import copy

globaly_data_base = dict()
globaly_access = dict()
global_VK_tracks = ["Serves You Right                   — Diamante"
                    "White Flag                         — Normandie"
                    "Roundtable Rival                   — Lindsey Stirling"
                    "Thnks fr th Mmrs                   — Fall Out Boy"
                    "I Hate Everything About You        — Three Days Grace"
                    "Ангел или демон                    — СЛОТ"
                    "Evidence Acoustic Version          — Prime Circle"
                    "Shook — Thousand Foot Krutch ve Me — About Monsters"
                    "feat. Oscar Porter                 — Shallowsky, Oscar Porter"
                    "Her Last Suggestions               — Staple R"
                    "Feel                               — Lies of P"
                    "CAST AWAY                          — From Fall to Spring"
                    "Paradox ( Vinland Saga ) Cover     — Binou SZ, Aoi Shiro"
                    "Whispers in the Dark Radio Edit    — Skillet"
                    "Температура                        — Три дня дождя, polnalyubvi"
                    "Wildfire (Russian Ver.)            — Sati Akura"
                    "DARK ARIA - Hardstyle              — Enmity, crypvolk"
                    "Снег в большом городе              — STERVELL"
                    "We Are Our Mountains               — Michael Night"
                    "The Scarlett Syndrome              — Leader"
                    ]
Now_in_some_account = False
class profile:
    """Реализация функций страницы пользователя"""

    def __init__(self, new_name="", new_surname="", new_middle_name=""):
        """Личная информация пользователя."""
        self.name = new_name
        self.surname = new_surname
        self.middle_name = new_middle_name

        self.date_birth = [0, 0, 0]

        self.place_birth = ""
        self.telephone = ""
        self.place_study = ""

        self.favorite_films = []
        self.count_films = 0
        self.favorite_music = []
        self.count_music = 0
        self.favorite_books = []
        self.count_books = 0
        self.apply_friends = []
        self.app_fr = 0

        """Информация o странице пользователя."""
        self.friends = []
        self.count_friends = 0
        self.posts = []
        self.subscribers = []
        self.count_subscribers = 0
        self.active_new_list = []
        self.active_messengers = dict()
        self.new_messengers = 0
        self.new_visitors = 0


    def get_information_about_profile(self):
        print("Full name", end=': ')
        print(self.name, end=' ')
        print(self.surname, end=' ')
        print(self.middle_name)
        if (self.date_birth[0] == 0):
            print("Дата рождения не указана")
        else:
            print(*self.date_birth)

    def get_new_messengers(self):
        to_r = self.new_messengers
        self.new_messengers = 0
        return to_r

    def get_new_visiotrs(self):
        to_r = self.new_visitors
        self.new_visitors = 0
        return to_r

    def show_news(self):
        for c in self.active_new_list:
            print(c)
        self.active_new_list.clear()

    """Имя"""

    def get_name(self):
        if self.name != "":
            return self.name
        else:
            # Если пользователь удалит имя
            return "Имя не указано"

    def delete_name(self):
        self.name = ""

    def change_name(self, new_name):
        self.name = new_name

    """Фамилия"""

    def get_surname(self):
        if self.surname != "":
            return self.surname
        else:
            return "Фамилия не указана"

    def delete_surname(self):
        self.surname = ""

    def change_surname(self, new_surname):
        self.surname = new_surname

    """Отчество"""

    def get_middle_name(self):
        if self.middle_name != "":
            return self.middle_name
        else:
            return "Отчество не указано"

    def delete_middle_name(self):
        self.middle_name = ""

    def change_middle_name(self, new_middle_name):
        self.middle_name = new_middle_name

    """Дата рождения"""

    def get_date_birth(self):
        return self.date_birth

    def delete_date_birth(self):
        for i in range(3):
            self.date_birth[i] = 0

    def change_date_birth(self, new_date_birth):
        self.date_birth = copy.copy(new_date_birth)

    def print_date_birth(self):
        if self.date_birth[0] != 0:
            print(self.date_birth[0], ".",
                    self.date_birth[1], ".",
                    self.date_birth[2],
                    sep=''
                )
        else:
            print("Дата рождения не указана.")

    """Место рождения"""

    def get_place_birth(self):
        if self.place_birth != "":
            return self.place_birth
        else:
            return "Метсто рождения не указано"

    def change_place_birth(self, new_place_birth):
        self.place_birth = new_place_birth

    def delete_place_birth(self):
        self.place_birth = ''

    """Телефон"""

    def get_telephone(self):
        if self.telephone != "":
            return self.telephone
        else:
            return "Телефон не указан"

    def change_telephone(self, new_telephone):
        self.telephone = new_telephone

    def delete_telephone(self):
        self.telephone = ''

    """Место учёбы"""

    def get_place_study(self):
        if self.place_study != "":
            return self.place_study
        else:
            return "Место учебы не указано"

    def change_place_study(self, new_place_study):
        self.place_study = new_place_study

    def delete_place_study(self):
        self.place_study = ''

    """Фильмы"""

    def add_film(self, new_film):
        self.count_films += 1
        self.favorite_films.append(new_film)

    def get_num_films(self):
        return self.count_films

    def get_films(self):
        return self.favorite_films

    def print_films(self):
        if len(self.favorite_films) != 0:
            for i in range(len(self.favorite_films)):
                print(i+1, ").", self.favorite_films[i])
        else:
            print("Фильмы не указаны.")

    def exclude_film(self, film):
        self.favorite_films.remove(self.favorite_films.index(film))

    """Музыка"""

    def add_music(self, new_music):
        self.count_music += 1
        self.favorite_music.append(new_music)

    def get_num_music(self):
        return self.count_music

    def get_music(self):
        return self.favorite_music

    def print_music(self):
        if len(self.favorite_music) != 0:
            for i in range(len(self.favorite_music)):
                print(i+1, self.favorite_music[i])
        else:
            print("Музыка не указана.")

    def exclude_music(self, music):
        self.favorite_music.remove(self.favorite_music.index(music))

    """Книги"""

    def add_books(self, new_books):
        self.count_books += 1
        self.favorite_books.append(new_books)

    def get_num_books(self):
        return self.count_books

    def get_books(self):
        return self.favorite_books

    def print_books(self):
        if len(self.favorite_books) != 0:
            for i in range(len(self.favorite_books)):
                print(i+1, self.favorite_books[i])
        else:
            print("Книги не указаны.")

    def exclude_book(self, book):
        self.favorite_books.remove(self.favorite_books.index(book))

    # """Информация o странице пользователя."""
    #       self.friends = []
    #       self.posts = []
    #       self.subscribers = []
    """Друзья"""

    def add_friend(self, new_friend):
        self.friends.append(new_friend)

    def get_num_friends(self):
        return self.count_friends

    def get_friends(self):
        return self.friends

    def exclude_friend(self, friend):
        self.friends.remove(self.friends.index(friend))

    def inc_apply_friends(self, friend):
        self.app_fr += 1
        self.apply_friends.append(friend)

    def get_apply_friends(self):
        return self.apply_friends

    def num_apply_friends(self):
        return self.app_fr

    """Посты"""

    def add_posts(self, new_post):
        self.posts.append(new_post)

    def get_num_posts(self):
        return len(self.posts)

    def get_posts(self):
        return self.posts

    def print_posts(self):
        if len(self.posts) != 0:
            for i in range(len(self.posts)):
                print(self.posts[i])
        else:
            print("Постов нет.")

    def exclude_post(self, post):
        self.posts.remove(self.posts.index(post))

    """Подписчики"""

    def add_subscriber(self, new_subscriber):
        self.count_subscribers += 1
        self.subscribers.append(new_subscriber)

    def get_num_subscribers(self):
        return self.count_subscribers

    def get_subscribers(self):
        return self.subscribers

    def print_subscribers(self):
        if len(self.subscribers) != 0:
            for i in range(self.count_subscribers):
                print(self.subscribers[i])
        else:
            print("Подписчиков нет.")

    def customize_account(self):
        typec = -1
        while typec != 8:
            print("1. Если хотите поменять имя")
            print("2. Если хотите поменять фамилию")
            print("3. Если хотите поменять пароль")
            print("4. Поменять дату рождения")
            print("5. Если хотите поменять аккаунт")
            print("6. Выйти из настроек")
            typec=int(input())
            if typec == 1:
                print("Введите новое имя")
                new_name=input()
                profile.change_name(self,new_name)
                print("Имя успешно изменено")
            if typec == 2:
                print("Введите новую фамилию")
                new_surname=input()
                profile.change_surname(self, new_surname)
                print("Фамилия успешно изменена")
            if typec == 3:
                print("Введите ваш логин")
                login = input()
                print("Введите новый пароль")
                # не забыть тут еще сделать чтобы обновлялось в глобальной базе
                new_pass = input()
                print("Введите новый пароль еще раз")
                new_pass2 =input()
                if (new_pass != new_pass2):
                    print("Пароли не совпадают")
                    continue
                globaly_access[login]=new_pass
                print("Пароль успешно изменен")
            if typec==6:
                return 0


def add_account():
    print("Введите имя нового пользователя")
    name = input()
    print("Введите фамилию нового пользователя")
    surname = input()
    print("Введите отчество нового пользователя")
    middlename = input()
    print("Введите логин")
    login = input()
    print("Введите пароль")
    password = input()
    print("Новый пользователь создан")
    New_Account = profile(name, surname, middlename)
    globaly_access[login] = password
    globaly_data_base[login] = New_Account
    return


def Account_Functions(login):

    print("Рады видеть вас снова в сети")
    profile = globaly_data_base[login]
    print("У вас целых", end=' ')
    print(profile.get_new_messengers(), end=' ')
    print("новых сообщений")
    print("За последние несколько часов вашу страницу посетили", end=' ')
    print(profile.get_new_visiotrs(), end=' ')
    print("человек")
    while True:
        print("1. Мой профиль")
        print("2. Новостная лента")
        print("3. Сообщения")
        print("4. Друзья")
        print("5. Подписчики")
        print("6. Группы")
        print("7. Музыка")
        print("8. Настройки")
        print("9. Дополнительная информация")
        print("10. Выйти")
        it = int(input())
        if it == 1:
            profile.get_information_about_profile()

        if it == 2:
            profile.show_news()

        if it == 3:
            print("Функция в разработке")

        if it == 4:
            func_friends(profile)
            
        if it == 5:
            func_subcribers(profile)
        if it == 6:
            print("Функция в разработке")
        if it == 7:
            music(profile)
        if it == 8:
            profile.customize_account()
        
        if it == 9:
            Additional_information(profile)
            
        if it == 10:
            print("Ждем назад, до свидания")
            break

def func_subcribers(prof):
    print("Подписчики")
    prof.print_subscribers()

def music(prof):
    while True:
        print("Музыка")

        print("Ваша любимая музыка:")
        print("Количество треков:", prof.get_num_music())
        prof.print_music()

        print("1. Удалить некоторые треки из списка")
        print("2. Удалить все треки")
        print("3. Включить трек")
        print("4. Добавить трек из ВК")
        print("5. Выйти из музыки.")

        inst = int(input())

        if inst == 1:
            print("Введите порядковые номера треков, которые вы хотите удалить")
            some_track = list(map(int, input().split()))

            print("Вы уудалили:")
            for i in range(len(prof.get_music())):
                if i+1 in some_track:
                    prof.exclude_music(prof.get_music()[i])
                    print(prof.get_music()[i], "\n")

        if inst == 2:
            for track in prof.get_music():
                prof.exclude_music(track)
                print("Удалены все треки")

        if inst == 3:
            print("Введите порядковый номера трека, которые вы хотите включить")
            track_number = int(input()) 
            print("Вы включили трек:", prof.get_music()[track_number-1])

        global global_VK_tracks
        if inst == 4:
            print("Музыка VK:")

            for track_VK in global_VK_tracks:
                print(track_VK)

            print("Выбирите номера треков, которые вы хотели бы добавить к cebe на страницу")

            music = list(map(str, input().split()))

            for i in range(len(global_VK_tracks)):
                if i+1 in music:
                    prof.add_music(global_VK_tracks[i])
        
        if inst == 6:
            break


def Additional_information(prof):
    #"""Место рождения"""
    #"""Телефон"""
    #"""Место учёбы"""
    #"""Фильмы"""
    #"""Музыка"""
    #"""Книги"""
    #"""Подписчики"""
    while True:
        print("Дополнительная информация o вас")
        print("1. Место рождения")
        print("2. Дата рождения")
        print("3. Место учёбы")
        print("4. Телефон")
        print("5. Фильмы")
        print("6. Книги")
        print("7. Выйти из дополнительной информации")
        instruction = int(input())


        if instruction == 1:
            print("1. Место рождения")
            print(prof.get_place_birth())

            print("1. Изменить")
            print("2. удалить")
            inst = int(input())

            if inst == 1:
                print("Введите место рождения:")
                new_place_birth = input()
                prof.change_place_birth(new_place_birth)

            if inst == 2:
                prof.delete_place_birth()


        if instruction == 2:
            print("Дата рождения")
            prof.print_date_birth()

            print("1. Изменить")
            print("2. удалить")

            inst = int(input())

            if inst == 1:
                print("Введите три числа через пробел:")
                new_date = list(map(int, input().split()))
                prof.change_date_birth(new_date)

            if inst == 2:
                prof.delete_date_birth()


        if instruction == 3:
            print("3. Место учёбы")
            print(prof.get_place_study())
            
            print("1. Изменить")
            print("2. удалить")

            inst = int(input())

            if inst == 1:
                print("Введите телефон:")
                new_place_study = input()
                prof.change_place_study(new_place_study)
                
            if inst == 2:
                prof.delete_place_study()

        if instruction == 4:
            print("4. Телефон")
            print(prof.get_telephone())
            
            print("1. Изменить")
            print("2. удалить")
            inst = int(input())
            
            if inst == 1:
                print("Введите телефон:")
                new_telephone = input()
                prof.change_telephone(new_telephone)
                
            if inst == 2:
                prof.delete_telephone()


        if instruction == 5:
            print("5. Ваши любимые Фильмы")
            print("Количество фильмов: ", prof.get_num_films())

            prof.print_films()

            print("1. Добавить фильмы в список")
            print("2. удалить некоторые фильмы")
            print("3. удалить все фильмы")

            inst = int(input())

            if inst == 1:
                print("Введите фильмы через пробел:")
                films = list(map(str, input().split()))
                for new_film in films:
                    prof.add_film(new_film)

            if inst == 2:
                print("Введите порядковые номера фильмов, которые вы хотите удалить")
                some_films = list(map(int, input().split()))
                
                for i in range(len(prof.get_films())):
                    if i+1 in some_films:
                        prof.exclude_film(prof.get_films()[i])     

            if inst == 3:
                print("Удалены все фильмы")
                for films in prof.get_films():
                    prof.exclude_film(films)

        if instruction == 6:
            print("6. Книги")
            print("Количество книг: ", prof.get_num_books())
            prof.print_books()

            print("1. Добавить книги в список")
            print("2. удалить некоторые книги")
            print("3. удалить все книги")

            inst = int(input())

            if inst == 1:
                print("Введите книги через пробел:")
                books = list(map(str, input().split()))
                for new_book in books:
                    prof.add_books(new_book)

            if inst == 2:
                print("Введите порядковые номера книг, которые вы хотите удалить")
                some_books = list(map(int, input().split()))

                for i in range(len(prof.get_books())):
                    if i+1 in some_books:
                        prof.exclude_book(prof.get_books()[i])

            if inst == 3:
                print("Удалены все книги")
                for book in prof.get_books():
                    prof.exclude_book(book)
        
        if instruction == 7:
            break


def func_friends(profile):

    while True:
        print("Друзья")
        print("1. Добавить в друзья или в подписчики")
        print("2. Удалить из друзей")
        print("3. Подать заявку в друзья")
        print("4. Заявки в друзья")
        print("5. Получить список друзей")
        print("6. Выйти")

        it = int(input())

        # "1. Добавить в друзья или в подписчики"
        if it == 1:

            if len(globaly_data_base) == 1:
                print("В ВКонтакте зарегистрированы только вы, добавлять в друзья некого")
            else:

                fr_count = 0

                for friend in profile.get_apply_friends():
                    fr_count += 1
                    print(fr_count, friend.get_name(),
                        friend.get_surname(),
                        friend.get_middle_name()
                        )

                print("1. Добавить в друзья всех")
                print("2. Добавить в подписчики всех")
                print("3. Добавить в подписчики некоторых")
                print("4. Никого не добавлять в друзья")
                print("5. Добавить некоторых в друзья")

                it = int(input())

                if it == 1:
                    for friend in profile.get_apply_friends():
                        profile.add_friend(friend)
                    print("Добавлены все")

                if it == 2:
                    for person in profile.get_apply_friends():
                        profile.add_subscriber(person)
                    print("Вы добавили всех в подписчики")
                if it == 3:
                    print("Перечислите номера тех, кого вы хотите добавить сейчас:")
                    some_friends = list(map(int, input().split()))
                    for i in range(profile.num_apply_friends()):
                        if i + 1 in some_friends:
                            profile.add_subscriber(profile.get_apply_friends()[i])
                    
                if it == 4:
                    print("Вы никого не добавили")

                if it == 5:
                    print("Перечислите номера тех, кого вы хотите добавить сейчас:")
                    some_friends = list(map(int, input().split()))
                    for i in range(profile.num_apply_friends()):
                        if i + 1 in some_friends:
                            profile.add_friend(profile.get_apply_friends()[i])

        # "2. Удалить из друзей"
        if it == 2:
            print("Введите имя, фамилию, отчество пользователя, которого хотите удалить из друзей")
            name, surname, middle_name = input().split()
            flag = True
            for account in globaly_data_base.values():
                if account.get_name() == name and \
                        account.get_surname() == surname and \
                        account.get_middle_name() == middle_name:
                    profile.exclude_friend(account)
                    print("Вы удалили: ",
                        account.get_name(),
                        account.get_surname(),
                        account.get_middle_name()
                        )
                    flag = False
            if flag:
                print("В ваших друзьях на было такого пользователя")

        if it == 3:
            print("Введите имя, фамилию, отчество пользователя, кому хотите подать заявку в друзья")
            name, surname, middle_name = input().split()
            flag = True
            flag1 = True
            for account in globaly_data_base.values():
                if account.get_name() == name and \
                        account.get_surname() == surname and \
                        account.get_middle_name() == middle_name:
                    if not (profile in account.get_apply_friends()):
                        account.inc_apply_friends(profile)
                        print("Вы подали завку в друзья пользователю: ",
                            account.get_name(),
                            account.get_surname(),
                            account.get_middle_name()
                            )
                    else:
                        print("Вы уже подавали заявку в друзья этому пользователю")
                    flag = False
            if flag:
                print("такого пользователя нет")

        if it == 4:
            if profile.num_apply_friends() == 0:
                print("Заявок в друзья нет")
            else:
                print("Заявки в друзья", profile.num_apply_friends())

        if it == 5:
            print("Количество друзей:", profile.get_num_friends())
            if profile.get_num_friends() != 0:
                for f in profile.get_friends():
                    f.get_information_about_profile()
                    print()
            else:
                print("Вы ещё не добавили никого.")

        if it == 6:
            break

def welcome_function():
    while True:
        print("Добро пожаловать в социальную сеть вконтакте")
        print("Доступные функции для пользователя:")
        print("1. Создать аккаунт")
        print("2. Войти в уже существующий аккаунт")
        print("3. Завершить программу.")

        it = int(input())

        if it == 3:
            exit()

        if it == 1:
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



