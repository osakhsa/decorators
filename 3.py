correct_password = "qwertyuiop123"


def check_password(func):
    def wrapper(*args, **kwargs):
        user_password = input("Введите пароль: ")
        if user_password == correct_password:
            func(*args, **kwargs)
        else:
            print("В доступе отказано.")
    return wrapper


@check_password
def func0args():
    print("There are 2 secret codes.")


@check_password
def func1arg_int(num):
    print("Secret code 1:", num+31)


@check_password
def func1arg_str(fraze):
    print("Secret code 2:", fraze.count("е"))


@check_password
def func2kwargs(key1=0, key2="Всероссийская олимпиада школьников"):
    print("Secret codes:", key1+31, key2.count("е"))


func0args()
func1arg_int(779865)
func1arg_str("Я пришёл к тебе с приветом рассказать, что солнце встало")
func2kwargs(key1=779865, key2="Я пришёл к тебе с приветом рассказать, что солнце встало")
