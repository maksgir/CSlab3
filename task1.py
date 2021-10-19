import os
import re

EMOJI = '=-\('


def test_loading(num_of_test):
    name = 'test' + str(num_of_test)
    fullname = os.path.join('data1', name)
    s = ''.join(open(fullname, 'r', encoding='utf8').readlines())
    return s


def count_smiles(num_of_test):
    s = test_loading(num_of_test)
    return len(re.findall(EMOJI, s))


num_of_smiles_in_test1 = count_smiles(1)  # Должно быть 7
num_of_smiles_in_test2 = count_smiles(2)  # Должно быть 37
num_of_smiles_in_test3 = count_smiles(3)  # Должно быть 110 - 1
num_of_smiles_in_test4 = count_smiles(4)  # Должно быть 33
num_of_smiles_in_test5 = count_smiles(5)  # Должно быть 144

print(num_of_smiles_in_test1)
print(num_of_smiles_in_test2)
print(num_of_smiles_in_test3)
print(num_of_smiles_in_test4)
print(num_of_smiles_in_test5)
