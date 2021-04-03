import time


def time_checker(func):

    def wrapper(**kwargs):
        t0 = time.time()
        func(**kwargs)
        t1 = time.time()
        print("Time elapsed:", t1-t0, "seconds")
    return wrapper


@time_checker
def useful_function(number):
    # number = kwargs['number']
    counter = 0
    for i in range(number+1):
        for k in range(i+1, number+1):
            counter += i * k
    counter = 1000000000
    print("Very useful function finished its very useful work! Bravo!")


useful_function(number=int(input()))
