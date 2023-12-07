import os


def funkcja(path):
    with open(path, 'r') as f:
        zmienna = f.read()
    slowa = zmienna.split()
    return len(slowa)





path = r'd:\Udemy\myfile.txt'

with open(path, 'x') as f:
    f.write('Jakiś krótki tekst co zawiera siedem słów.')


# if os.path.isfile(path):
#     ilosc_slow = funkcja(path)  # zwraca ilosc słów
#     print(f'File {path} has {ilosc_slow} words')


# result = os.path.isfile(path) and funkcja(path)
# print(f'File {path} has {result} words')
os.path.isfile(path) and print(f'File {path} has {funkcja(path)} words')

os.remove(path)


# with open(path, 'r', encoding='utf-16') as plik:
#     zmienna = plik.read()
#     zmienna = zmienna.split()
