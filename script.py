#!/usr/bin/env python2

import csv
import os
import shutil
from collections import namedtuple
from jinja2 import Template


shutil.rmtree('./Cartes')
os.mkdir('./Cartes')

with open('_carte.html') as fd:
    html = Template(fd.read())

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
                card = Card(*line)
                variables = dict(
                    (key, value.decode('utf-8') if value != 'x' else '')
                    for key, value in card._asdict().items())
                with open('./Cartes/%s%02i - %s.html' % (
                        name[0], i, card.title), 'w') as fd:
                    fd.write(html.render(**variables).encode('utf-8'))
