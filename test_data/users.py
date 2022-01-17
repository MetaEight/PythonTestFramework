users = [
    {"name": "user_1", "username": "standard_user", "password": "secret_sauce"},
    {"name": "user_2", "username": "locked_out_user", "password": "secret_sauce"},
    {"name": "user_3", "username": "problem_user", "password": "secret_sauce"}
]


def get_user(name):
    try:
        return next(user for user in users if user["name"] == name)
    except:
        raise Exception(f"Пользователь с таким именем {name} не найден")
