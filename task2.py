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


for i in range(1, 6):
    print(f'Тест {i} - {haiku_searching(i)}')

