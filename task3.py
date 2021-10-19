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


print(mail_analysing(1))
print(mail_analysing(2))
print(mail_analysing(3))
print(mail_analysing(4))
print(mail_analysing(5))
print(mail_analysing(6))
