#!/bin/bash
rst2html.py -l fr --link-stylesheet --initial-header-level 2 --stylesheet style.css regle.rst > regle.html
weasyprint regle.html regle.pdf
pdf2ps regle.pdf regle.ps
psbook regle.ps regle_book.ps
psnup -2 -w21cm -h25cm -W10.5cm -H25cm regle_book.ps regle_booklet.ps
ps2pdf regle_booklet.ps regle_booklet.pdf
rm *.ps
