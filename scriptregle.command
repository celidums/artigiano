DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR
/usr/local/bin/rst2html.py -l fr --link-stylesheet --initial-header-level 2 --stylesheet Style/style_regle.css regle.rst > regle.html
/usr/local/bin/python /usr/local/bin/weasyprint regle.html regle.pdf