# ekorbi
from bs4 import BeautifulSoup
import requests
import soupsieve
urls = ['http://hanzidb.org/character-list/hsk']
page = 2
for url in range(1,27):
    url = 'http://hanzidb.org/character-list/hsk'+"?page="+ str(page)
    urls.append(url)
    page+=1
    
full = ' '
for url in urls:
    res = requests.get(url)
    res.encoding = 'utf-8'
    content = res.text
    soup = BeautifulSoup(content,'html.parser')
    rows = soup.findAll('tr')
    full_list = []
    for row in rows:
        full_list.append(row.td)
    level_one = full_list[1:]

    hanzi_list = []
    pinyin = [] 
    cnt = 0
    definition = []
    for data in level_one:
        hanzi = data.text
        hanzi_list.append(hanzi)

    for trow in rows:
        tdata = trow.findAll('td')[1:2]
        if tdata:
            el = tdata[0].text
            pinyin.append(el)
    
    for trow in rows:
        dfn = trow.findAll('td')[1:3]
        if dfn:
            word = dfn[1].text.replace(',',' ')
            definition.append(word)
    
    for i in range(1,len(rows)):
      full += ("{:<7}".format(str(cnt+1)) + " {:<7}".format(hanzi_list[cnt])+ "{:<7}".format(pinyin[cnt]) + "{:<9}".format(definition[cnt]) + "\n")
      cnt+=1
      
with open('hanzi.txt','w',encoding='utf-8') as fh:
    header = "{:<7}".format(" ") + "{:<7}".format("Hanzi")  + "{:<10}".format("Pinyin") + "Definition" + "\n"
    fh.write(header)
    fh.write(full)
    print("Finished,all characters displayed!")