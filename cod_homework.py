# -*- coding: utf-8 -*-

# блоки кода

x, y = 10, 29

if x < 0:
    print('Х меньше нуля')
    z = x ** 2 + y
else:
    print('Х больше нуля')
    z = x - y
print('Результат', z)

# ср. с С++

# if (x < 0) { printf('Меньше нуля\n'); z = x**2 + y; }
# else { printf('Больше нуля\n'); z = x - y; } printf('Получается\n', z)

# вложенные блоки кода

name = input('Введите свое имя: ')
if name == 'Ола':
    print('Привет, Ола!')
else:
    if name == 'София':
        print('Привет, София!')
    else:
        if name == 'Катя':
            print('Привет, Катя!')
        else:
            print('Привет, аноним!')

# оператор pass

if x < 0:
    if y > 0:
        z = - x + y
    else:
        z = - x - y
else:
    z = x + y

# соглашения о стиле кода
# PEP8 (Python Enhancement Proposal 8) - описан "правильный" стиль программирования в пайтон
# https://www.python.org/dev/peps/pep-0008/

# 4 пробела на каждый уровень отступа

if x < 0:
    if y > 0:
        pass
    else:
        print('направо!')
else:
    print('стой!')

# Максимальная длина строки

my_poem = ['Варкалось, хливкие шорьки пырялись по наве', 'И хрюкотали зелюки как мюмзики в мове',
           'О бойся Бармаглота, сын! Он так свирлеп и дик', 'А в глуше рымит исполин - Злопастный Брандашмыг!', ]

# пробелы в операторах

x = 2
y = x * x + 1
is_big = x >= 3000

x = my_poem[-1]
print(x)
my_list = [2, 3, 4, 5, 6, ]

# reformat кода

x, y = 3, 8

if x == 3:
    print(42)

if x < 0:
    if y > 0:
        print('налево!')
    else:
        print('направо!')
else:
    print('стой!')

# названия переменных

pets = 34
if pets > 10:
    print('I need more space for my pets!')

favorite_pets = ['cat', 'wolf', 'ostrich']
if 'lion' in favorite_pets:
    print('Wow!')




# рекомендации PEP8

# b (одиночная маленькая буква)
# B (одиночная заглавная буква)
# но лучше использовать только такие однобуквенные имена
#   i j k - для циклов
#   x y z - для координат

# никогда не используйте в названиях переменных одиночные l, I, O  !
h = 34
g = 43
if h > g:
    print('больше')
p = 9
if p > 0:
    print("больше")

# lowercase (слово в нижнем регистре)
# lower_case_with_underscores (слова из маленьких букв с подчеркиваниями)
# UPPERCASE (заглавные буквы)
# UPPERCASE_WITH_UNDERSCORES (слова из заглавных букв с подчеркиваниями)

# CapitalizedWords (слова с заглавными буквами, или CapWords, или CamelCase).
#   Замечание: когда вы используете аббревиатуры в таком стиле, пишите все буквы аббревиатуры заглавными —
#   HTTPServerError лучше, чем HttpServerError.

# mixedCase (отличается от CapitalizedWords тем, что первое слово начинается с маленькой буквы)
# Capitalized_Words_With_Underscores (слова с заглавными буквами и подчеркиваниями — уродливо!)


# автоматическое переименование в PyCharm и подсказки - вам не нужно набирать длинные названия переменных

pets_ = ['cat', 'wolf', 'ostrich']
if 'lion' in pets_:
    print('Wow!')

# В каждой уважающей себя компании есть style guide (стайл-гайд) - руководство по стилю написания кода.
# Практически все они основываются на PEP8, с небольшими исключениями, принятыми в этой команде.
# Как пример стайл-гайда небольшой компании рекомендую почитать
# https://github.com/best-doctor/guides/blob/master/guides/python_styleguide.md
