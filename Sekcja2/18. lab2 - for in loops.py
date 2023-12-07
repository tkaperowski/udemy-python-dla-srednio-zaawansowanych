import os
import urllib.request

data_dir = r'd:\Udemy\strony_www'
pages = []
pages.append({ 'name': 'mobilo', 'url': 'http://www.mobilo24.eu/'})
pages.append({ 'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/'})
pages.append({ 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'} )

for page in pages:
    file_name = '{}.html'.format(page['name'])
    # file_name = f'{page["name"]}.html'
    print(file_name)
    path = os.path.join(data_dir, file_name)
    print(path)
    try:
        print('Processing: {} into {}...'.format(page['url'], file_name))
        urllib.request.urlretrieve(page['url'], path)
        print('...done!')
    except:
        print('Failure processing web page: {}'.format(page['url']))
        print('Stopping the process!!!')
        break
else:
    print('URL saved to files :)')
