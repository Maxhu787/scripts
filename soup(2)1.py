# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
print(tags[0].contents[0])
html = urllib.request.urlopen(tags[2].get('href', None), context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
print(tags[17].contents[0])
html = urllib.request.urlopen(tags[2].get('href', None), context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
print(tags[17].contents[0])
html = urllib.request.urlopen(tags[2].get('href', None), context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
print(tags[17].contents[0])
html = urllib.request.urlopen(tags[2].get('href', None), context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
print(tags[17].contents[0])
html = urllib.request.urlopen(tags[2].get('href', None), context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
print(tags[17].contents[0])
html = urllib.request.urlopen(tags[2].get('href', None), context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
print(tags[17].contents[0])
