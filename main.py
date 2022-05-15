# Написати декоратор для будь якої функції, що буде зберігати історію викликів функцій у файлі.
# Тобто всі функції що будуть задекоровані цим декоратором з кожним викликом мають записути у файл наступний рядок:
# {Function name} was called with args {args & kwargs} at {time} and return result {result}

def deco(func):
    def wrapper(*args, **kwargs):
        from datetime import datetime
        res = func(*args, **kwargs)
        func_call_log = open('func_call_log.txt', 'a')
        func_call_log.write(
            f'{func.__name__} was called with args {args, kwargs} at {datetime.today()} and return result {res}\n'
        )
        func_call_log.close()
        return res
    return wrapper


@deco
def my_func1(a, b, c, d, e):
    return a * b + c + d * e


@deco
def my_func2(x, y, z):
    return (x + y) * z


@deco
def my_func3(f, g, h):
    return f * g + h


print(my_func1(2, 3, d=3, e=2, c=5))
print(my_func2(1, z=3, y=2))
print(my_func3(5, h=2, g=3))
