correct_password = "qwertyuiop123"


def check_password(func):

    def wrapper(*args, **kwargs):
        user_password = input("Введите пароль: ")
        if user_password == correct_password:
            func(*args, **kwargs)
        else:
            print("В доступе отказано.")
    return wrapper


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# fibonacci_copy = fibonacci


@check_password
def first_call(number):
    return fibonacci(number)


print(first_call(10))
