
from markdown import markdown

from xhtml2pdf import pisa

import os

import codecs

CUR_DIR = os.getcwd()

FILES_TREE = []

final_file = codecs.open("final.html", "a",              # Append mode.
                          encoding='utf-8',
                          errors='xmlcharrefreplace')

#with open("final.html","")
for root, dirs, files in os.walk(CUR_DIR):
    for mdfile in files:
        file_name = os.path.join(root, mdfile)
        if(file_name.split(".")[-1] == 'md'):
            md_file = codecs.open(file_name, mode='r', encoding='utf-8')
            md_data = markdown(md_file.read())
            final_file.write(md_data)
            md_file.close()

final_file = codecs.open("final.html", "a",              # Append mode.
                          encoding='utf-8',
                          errors='xmlcharrefreplace')
dest = open("clrs_ans", "w+b")
_pdf = pisa.CreatePDF(final_file.read(), dest = dest)
