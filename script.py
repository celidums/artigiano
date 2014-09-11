#!/usr/bin/env python2.7

import csv
import os
import shutil
import weasyprint
from collections import namedtuple
from jinja2 import Template


if os.path.exists('./Cartes'):
    shutil.rmtree('./Cartes')
os.mkdir('./Cartes')

with open('_carte.html') as fd:
    html = Template(fd.read().decode('utf-8'))

Card = namedtuple('Card', [
    'type', 'title', 'material', 'value', 'ma_points', 'sp_points',
    'mi_points', 'text'])

for filename in os.listdir('.'):
    if not filename.startswith('_') and filename.endswith('.csv'):
        name = filename[:-4]
        with open(filename) as fd:
            reader = csv.reader(fd)
            reader.next()
            for i, line in enumerate(reader):
                code = '%s%02i' % (name[0], i + 1)
                card = Card(*line)
                variables = dict(
                    (key, value.decode('utf-8') if value != 'x' else '')
                    for key, value in card._asdict().items())
                variables['code'] = code
                output_file = os.path.join(
                    'Cartes', '%s - %s' % (code, card.title))
                print('Rendu de %s' % output_file)
                with open(output_file + '.html', 'w') as fd:
                    fd.write(html.render(**variables).encode('utf-8'))
                weasy = weasyprint.HTML(output_file + '.html')
                weasy.write_png(output_file + '.png', resolution=30)
