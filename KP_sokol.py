#!/usr/bin/python

import lxml.html
import urllib

URL="http://nod32.sokol.biz.ua/"

page = urllib.urlopen(URL).read()
doc = lxml.html.document_fromstring(page)

f = open('keys.txt', 'w')

username = doc.xpath ('//table/tbody/tr/td/p/text()')[4:][:1]
password = doc.xpath ('//table/tbody/tr/td/p/text()')[5:][:1]
result = 'Username:' + ''.join(username) + '\n' + 'Password:' + ''.join(password)
#print result 
f.write(result)

f.close()