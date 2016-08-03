#!/usr/bin/python

import lxml.html
import requests

URL="http://hhuu.net/"

page = requests.get(URL).text
parser = lxml.html.fromstring(page)
f = open('keys.txt', 'w')



#username = parser.cssselect('p')
#template = 'username: {}'
#for i in zip(username):
#    print(template.format(*[j.text for j in i]).strip())


#buf = [i for i in parser.cssselect('table.table1 td.new_table_tb_top')
#           if i.text.strip()]
#print (buf)

for i in parser.cssselect('body.compact product front p'):
    print(i.text)
    #f.write(i.text + '\n')

f.close()