#!/usr/bin/env python2.7

import csv
import os
import shutil
import weasyprint
from collections import namedtuple
from jinja2 import Template


if os.path.exists('./Rendus'):
    shutil.rmtree('./Rendus')
os.mkdir('./Rendus')

with open('_carte.html') as fd:
    html = Template(fd.read().decode('utf-8'))

Card = namedtuple('Card', [
    'type', 'material', 'value', 'ma_points', 'sp_points',
    'mi_points', 'title', 'text'])


for back_type in ('missions', 'autres'):
    print('Rendu du dos %s' % back_type)
    weasy = weasyprint.HTML('_dos_%s.html' % back_type)
    weasy.write_png(
        os.path.join(u'Rendus', 'dos_%s.png' % back_type), resolution=30)


for filename in os.listdir('.'):
    if not filename.startswith('_') and filename.endswith('.csv'):
        symbol, name = filename.decode('utf-8').split(' ', 1)
        name = name[:-4]
        with open(filename) as fd:
            reader = csv.reader(fd)
            reader.next()
            for i, line in enumerate(reader):
                code = u'%s%02i' % (symbol, i + 1)
                card = Card(*line)
                variables = dict(
                    (key, value.decode('utf-8') if value != 'x' else '')
                    for key, value in card._asdict().items())
                variables['code'] = code
                variables['symbol'] = symbol
                output_filename = (
                    u'%s - %s' % (code, variables['title'])
                    if variables['title'] else code)
                output_file = os.path.join(u'Rendus', output_filename)
                print('Rendu de %s' % output_filename)
                with open(output_file + '.html', 'w') as fd:
                    fd.write(html.render(**variables).encode('utf-8'))
                weasy = weasyprint.HTML(output_file + '.html')
                weasy.write_png(output_file + '.png', resolution=30)
