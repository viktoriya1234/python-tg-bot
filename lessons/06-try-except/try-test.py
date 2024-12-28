# print('N1')
# n1 = int(input())
# print('N2')
# n2 = int(input())
#
# try:
#     d = n1 / n2
#     print(d)
# except ZeroDivisionError:
#     print('Ділення на 0!')
# else:
#     print('Else!')
# finally:
#     print('Finally!')
#
# print('all work')


# f = None
# try:
#     with open('f1.txt') as file:
#         f = file.read()
# except FileNotFoundError:
#     with open('f1.txt', 'w') as file:
#         file.write('Значення по замовчуванню')
# finally:
#     if not f:
#         with open('f1.txt') as file:
#             f = file.read()
#
# print(f)


class FifeDivisionError(Exception):
    def __init__(self, message, error_code):
        super().__init__(message)
        self.error_code = error_code


def divide_number(a, b):
    if 5 == b:
        raise FifeDivisionError('Ділити на 5 не можна', 2024)
    return a / b

try:
    d = divide_number(12, 5)
    print(d)
except FifeDivisionError as e:
    print(f"Помилка: {e}")
    print(f"Код помилки: {e.error_code}")