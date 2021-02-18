#!/usr/bin/python

import lxml.html
import urllib
import re

URL="https://t.me/s/fornod"

page = urllib.urlopen(URL).read()
doc = lxml.html.document_fromstring(page)

data = doc.xpath ('//html/body/main/div/section/div[2]/div[1]/div[2]/div[2]/text()')
#print data

indx = 0
list=[]
username = ''
password = ''

for i in data:
        if i == 'ESET NOD32 Antivirus':
                indx = data.index(i)

for i in range(indx, indx+5):
        list.append(data[i])

for i in list:
        if re.match(r'Username',i):
                username = i
        if re.match(r'Password',i):
                password = i

# print username
# print password

f = open('keys.txt', 'w')
result = ''.join(username) + '\n' + ''.join(password)
f.write(result)
f.close()
