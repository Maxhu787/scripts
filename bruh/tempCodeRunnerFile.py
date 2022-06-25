import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url=input("Enter url:")

count=int(input('Enter count:'))
pos=int(input('Enter position:'))-1

urllist=list()

for i in range(count):
    html=urllib.request.urlopen(url)
    soup=BeautifulSoup(html,'html.parser')
    tags=soup('a')
    print('Retrieveing:',url)
    taglist=list()
    for tag in tags:
        y=tag.get('href',None)
        taglist.append(y)

    url=taglist[pos]

    urllist.append(url)

print("Last Url:",urllist[-2])