import selenium
from urllib.error import HTTPError
from urllib.error import URLError
from urllib.request import urlopen

try:
    html=urlopen('https://fstt.ac.ma/Portail2023/')
except HTTPError as e:
    print('Server not found')
except URLError as e:
    print('HTTP error: %s' % e)
else:
    print(html.read())
