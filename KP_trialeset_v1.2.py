#!/usr/bin/python

import lxml.html
#import requests
import urllib

URL="http://trialeset.ru/"

page = urllib.urlopen(URL).read()
doc = lxml.html.document_fromstring(page)

f = open('keys.txt', 'w')

username = doc.xpath ('//table[@class="table-main"]/tbody/tr/td/text()')[2:][:1]
password = doc.xpath ('//table[@class="table-main"]/tbody/tr/td/text()')[2:][:2][1:]
result = 'Username:' + ''.join(username) + '\n' + 'Password:' + ''.join(password)
#print result 
f.write(result)

f.close()
