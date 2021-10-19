import os
import re


def test_loading(num_of_test):
    name = 'test' + str(num_of_test)
    fullname = os.path.join('data2', name)
    s = ''.join(open(fullname, 'r', encoding='utf8').readlines())
    return s


def haiku_searching(num_of_test):
    text = test_loading(num_of_test)
    paragraph = re.split(r'\/', text)
    if len(paragraph) != 3:
        return 'Не хайку. Должно быть 3 строки.'
    vowels = []
    for s in paragraph:
        vowels.append(len(re.findall(r'[уеаоэяи]', s.lower())))
    if vowels == [5, 7, 5]:
        return "Хайку!"
    return "Не хайку."


print(haiku_searching(1))
print(haiku_searching(2))
print(haiku_searching(3))
print(haiku_searching(4))
print(haiku_searching(5))
