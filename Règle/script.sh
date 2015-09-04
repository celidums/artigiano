#!/bin/bash
rst2html.py -l fr --link-stylesheet --initial-header-level 2 --stylesheet style.css regle.rst > regle.html
weasyprint regle.html regle.pdf
