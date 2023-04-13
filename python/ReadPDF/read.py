# -*- coding: utf-8 -*-

# read pdf file

import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")

import PyPDF2

#opening of file and creation of read_file variable

pdf_file = open("AlN.pdf", "rb")
read_pdf = PyPDF2.PdfFileReader(pdf_file)

# command for know the pdf file number
number_of_page = read_pdf.getNumPages()

print number_of_page



 # kind of page pdf file of a page 0
page = read_pdf.getPage(4)

page_number = read_pdf.getPageNumber(page)
print page_number

page_mode = read_pdf.getPageMode()
print page_mode

# extract_content of page 0

page_content = page.extractText()
print page_content.encode("utf-8")

print "#############################"
#Other way of print symbol 
#print page_content.encode("ascii", "replace")

