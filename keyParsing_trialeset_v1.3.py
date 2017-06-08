#!/usr/bin/python

import lxml.html
import requests

URL="http://trialeset.ru/"

page = requests.get(URL).text
parser = lxml.html.fromstring(page)
f = open('keys.txt', 'w')

username = parser.cssselect('.key-text')[:1]
password = parser.cssselect('.key-text')[1:][:1]

template = 'Username:{}' + '\n' + 'Password:{}'
for i in zip(username, password):
#	print(template.format(*[j.text for j in i]).strip())
        f.write(template.format(*[j.text for j in i]).strip())

f.close()

