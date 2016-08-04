#!/usr/bin/python

import re

#import urllib
#URL="http://hhuu.net/"
#response = urllib.urlopen(URL)
#html = response.read()
#m = re.findall('\w+', html)
#print m

f = open('temp.int', 'r')
g = unicode(f.read(), 'utf-8')

username = re.search(r'Username:\w+.\w+', g)
password = re.search(r'Password:\w+', g)

#print username.group(0)
#print password.group(0)

k = open('keys.txt', 'w')
k.write(username.group(0) + '\n' + password.group(0))
f.close()
k.close()
