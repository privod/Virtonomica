from urllib.request import urlopen

import lxml.html as html
from pandas import DataFrame

domain = 'https://virtonomica.ru'
server = 'olga'
company = '6402898'
page = html.parse(urlopen('{}/{}/main/company/view/{}/unit_list'.format(domain, server, company)))

elem_list = page.getroot().find_class('wborder')

for elem in elem_list:
    print(elem.attrib, elem.tag)
    for field in elem.getchildren():
        print(field.attrib, field.tag, field.text)
