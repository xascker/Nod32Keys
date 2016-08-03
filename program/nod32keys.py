#!/usr/bin/python

import lxml.html
import requests

URL="http://trialeset.ru/"

page = requests.get(URL).text
parser = lxml.html.fromstring(page)
f = open('keys.txt', 'w')

#for i in parser.cssselect('table.table1 td.new_table_tb_top ')[:2]:
#    f.write(i.text + '\n')

username = parser.cssselect('table.table1 td.new_table_tb_top ')[:1]
password = parser.cssselect('table.table1 td.new_table_tb_top ')[1:][:1]
template = 'username: {}' + '\n' + 'password: {}'
for i in zip(username, password):
    f.write(template.format(*[j.text for j in i]).strip())

f.close()