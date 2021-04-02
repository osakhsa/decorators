def upper_print(text):
    return print_copy(text.upper())


print_copy = print
print = upper_print
print("Я пришёл к тебе с приветом рассказать, что солнце встало")
