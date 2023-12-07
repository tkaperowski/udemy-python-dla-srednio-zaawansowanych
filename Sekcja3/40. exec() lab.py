import os
file_to_process = [r'D:\Udemy\Python dla srednio zaawansowanych\Sekcja3\math_sin_square.py', r'D:\Udemy\Python dla srednio zaawansowanych\Sekcja3\math_square_root.py']


# aaa = os.path.basename(file_to_process[0])
# print(aaa)

for i in file_to_process:
    print(i)
    aaa = os.path.basename(i)
    print(aaa)
    with open(aaa, 'r') as f:
        print(f)
        read = f.read()
    exec(read)