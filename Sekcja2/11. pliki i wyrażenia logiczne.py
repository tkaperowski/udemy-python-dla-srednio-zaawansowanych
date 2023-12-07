import os

path = r'd:\Udemy\mydata.txt'

# try:
#     os.remove(path)
# except FileNotFoundError:
#     print(f'File {path} not existing...')

'''
if os.path.isfile(path):
    print('File %s exists' % path)
else:
    print('File %s doesn\'t exist' % path )
    print(f'Creating a file {path}')    #f-string zalecany
    open(path, 'x').close()
    print(f'File {path} created')
'''

result = os.path.isfile(path) or open(path, 'x').close() # or alternatywa (jak dostanie true to kończy), and koniunkcja (sprawdza aż dostanie false)
print(result)