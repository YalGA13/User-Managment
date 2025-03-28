class User:
    def __init__(self, user_id: int, name: str):
        self._user_id = user_id
        self._name = name
        self._access_level = 'Сотрудник'

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, name: str):
        self._name = name

    def __str__(self):
        return f"Сотрудник: {self._user_id}, Имя: {self._name},  Уровень доступа: {self._access_level})"


class Admin(User):
    def __init__(self, user_id: int, name: str):
        super().__init__(user_id, name)
        self._access_level = 'Администратор'

    def add_user(self, user_list: list, user: User):
        if user not in user_list:
            user_list.append(user)
            print(f"Сотрудник {user.get_name()} идентификатор: {user.get_user_id()}) добавлен.")
        else:
            print(f"Сотрудник {user.get_name()} уже существует.")

    def remove_user(self, user_list: list, user_id: int):
        for user in user_list:
            if user.get_user_id() == user_id:
                user_list.remove(user)
                print(f"Сотрудник {user.get_name()} идентификатор: {user_id})  удален.")
                return
        print(f"Сотрудник с идентификатором {user_id} не найден.")





# Пример использования
if __name__ == "__main__":
    user1 = User(1, "Анфиса")
    user2 = User(2, "Альберт")
    user3 = User(3, "Борис")
    user4 = User(4, "Любовь")
    user5 = User(5, "Екатерина")
    user6 = User(6, "Сергей")
    admin1 = Admin(98, "Дмитрий")
    admin2 = Admin(99, "Владимир")

    users = [user1, user2, user3, user4, user5, user6 ]
    admins = [admin1,admin2]

    print("Первоначальные пользователи:")
    for user in users:
        print(user)
    for admin in admins:
        print(admin)

    new_user = User(7, "Михаил")
    admin1.add_user(users, new_user)
    new_user = User(8, "Антон")
    admin2.add_user(users, new_user)

    print("\nДобавленый сотрудник - Михаил:")
    for user in users:
        print(user)

    admin1.remove_user(users, 2 )

    print("\nУдаленный сотрудник - Альберт:")
    for user in users:
        print(user)
