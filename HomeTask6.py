# Написати функції:

# 1. Примає радіус кола, повертає довжину кола. Обробити випадки коли в радіус приходить не числом.
def circle_length(r):
    from math import pi
    try:
        c = 2 * pi * r
        return c
    except TypeError:
        return 'Radius must be numeric'


print(circle_length(5))
print(circle_length('s'))


# 2. Примає радіус кола, повертає площу кола. Обробити випадки коли в радіус приходить не числом.
def circle_square(r):
    from math import pi
    try:
        s = pi * r ** 2
        return s
    except TypeError:
        return 'Radius must be numeric'


print(circle_square(5))
print(circle_square('s'))


# 3. Приймає число, повертає чи є число поліндромом.
# Тобто з права на ліво і з ліва на право читається однаково. 12321 - це поліндром, 1234 - не поліндром.
def is_palindrome(n: int):
    if not type(n) == int:
        return "'n' must be integer"
    elif list(str(n)) == list(str(n))[::-1]:
        return 'Is a palindrome'
    else:
        return 'Is not a palindrome'


print(is_palindrome('d'))
print(is_palindrome(101))
print(is_palindrome(102))


# 4. Функція приймає число n яке більше 0. За допомогою рекурсії виводить всі числа що менші n але більші 0.
def recur(n: int):
    if not type(n) == int:
        return "'n' must be integer"
    elif n <= 1:
        return 'maximum recursion depth exceeded'
    elif n - 1 == 1:
        return 1
    return f'{n - 1} {recur(n - 1)}'


print(recur('s'))
print(recur(1))
print(recur(-10))
print(recur(10))


# 5. Написати функцію lambda що приймає x i y, а повертає x^2 + y^2
my_lambda = lambda x, y: x ** 2 + y ** 2
print(my_lambda(2, 3))

# 6. Написати функцію lambda що приймає слово і повертає його довжину.
my_lambda_len = lambda a: len(a)
print(my_lambda_len('programming'))

# 7. Написати map що перетворює всі числа в списку на строку.
lst = [123, 3456, 789012, 54.789]
lst = list(map(lambda x: str(x), lst))
print(lst)

# 8. Написати filter що залишає в списку тільки числа > 10
lst = [11, 2, 5, 34, 900, 3, 4, 100]
lst = list(filter(lambda x: x > 10, lst))
print(lst)

# 9. Є список слів, за допомогою map видалити з кожного слова всі букви "а" (abcd -> bcd )
# (2 способи з lambda і без ) ( підказка: викорисати метот replace )

# 1
lst = ['cat', 'anaconda', 'bank', 'America', 'Australia']
lst = list(map(lambda x: x.lower().replace('a', ''), lst))
print(lst)

# 2
lst = ['cat', 'anaconda', 'bank', 'America', 'Australia']
def replace_a(a):
    return a.lower().replace('a', '')

lst = list(map(replace_a, lst))
print(lst)

# 3
lst = ['cat', 'anaconda', 'bank', 'America', 'Australia']
lst = [i.lower().replace('a', '') for i in lst]
print(lst)

# 10. Є список слів, за допомогою filter залишити тільки ті слова в яких к-ть букв більша ніж 4.
# (2 способи з lambda і без )

# 1
lst = ['cat', 'anaconda', 'bank', 'America', 'Australia']
lst = list(filter(lambda x: len(x) > 4, lst))
print(lst)

# 2
lst = ['cat', 'anaconda', 'bank', 'America', 'Australia']
def more_then_4(a):
    return len(a) > 4

lst = list(filter(more_then_4, lst))
print(lst)

# 3
lst = ['cat', 'anaconda', 'bank', 'America', 'Australia']
lst = [i for i in lst if len(i) > 4]
print(lst)
