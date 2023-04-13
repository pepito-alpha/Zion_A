# -*- coding: utf-8 -*-

# read pdf file

import sys
import PyPDF2


#name of the pdf file given by user

namefile = raw_input("What is name of pdf file? (no write extension): ")

print ("the name of pdf file is " + namefile)

namefile = namefile +".pdf"

pdf_file = open(namefile, "rb")

#opening of file and creation of read_file variable
read_pdf = PyPDF2.PdfFileReader(pdf_file)

# command for know the pdf file number
number_of_page = read_pdf.getNumPages()

print ("PDF File has " + str(number_of_page) + " pages")

pageview = int(raw_input("what page do you want print in your screen?: "))

# kind of page pdf file of a page 
page = read_pdf.getPage(pageview)

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

