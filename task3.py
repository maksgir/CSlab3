import os
import re


def test_loading(num_of_test):
    name = 'test' + str(num_of_test)
    fullname = os.path.join('data3', name)
    s = ''.join(open(fullname, 'r', encoding='utf8').readlines())
    return s


def mail_analysing(num_of_test):
    mail = test_loading(num_of_test)
    a = re.fullmatch(r'[0-9A-Za-z._]+@[A-Za-z.]+\.[A-Za-z.]+',
                     mail)  # проверяем корректность почтового адреса а впринципе
    if not a:
        return 'Fail!'
    server = re.split(r'@', mail)
    return server[1]


for i in range(1, 7):
    print(f'Тест {i} - {mail_analysing(i)}')
