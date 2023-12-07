import os
import urllib.request

data_dir = r'd:\Udemy\strony_www'
pages = []
pages.append({ 'name': 'mobilo', 'url': 'http://www.mobilo24.eu/'})
pages.append({ 'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/'})
pages.append({ 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'} )
print(pages, type(pages))
print(pages[0]['url'])
print(pages[1]['name'])
pages.append({'name':'dupa', 'url':'wołowa'})
del pages[3]
print(pages)


for page in pages:
    path = rf'{data_dir}\{page["name"]}.html'
    print(path)
    try:
        urllib.request.urlretrieve(page['url'], path)
    except:
        print('URL error!!!')
        break
else:
    print('URL saved to files :)')
