#!/usr/bin/python

import lxml.html
import requests

URL="http://eset-key.ru/"

page = requests.get(URL).text
parser = lxml.html.fromstring(page)
f = open('keys.txt', 'w')

username = parser.cssselect('tr.tkeyc td')[:3][2:]
password = parser.cssselect('tr.tkeyc td')[3:][:1]

#for row in password:
#    print row.text

template = 'Username:{}' + '\n' + 'Password:{}'
for i in zip(username, password):
#	print(template.format(*[j.text for j in i]).strip())
        f.write(template.format(*[j.text for j in i]).strip())

f.close()

