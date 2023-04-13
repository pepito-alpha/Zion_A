# Este programa buca palabras o letras y las cuantifica

## -*- coding: utf-8 -*-
import sys

import PyPDF2

print("===========================================================")
print("\n            Cuantificador de Palabras o letras         \n")
print("===========================================================")


# pide al usuario el nombre del pdf, lo imprime el nombre en pantalla y lo abre

namefile = raw_input("What is name of pdf file? (no write extension): ")


namefile = namefile +".pdf"

pdf_file = open(namefile, "rb")

print("Info del documento:\n")

print ("the name of pdf file is " + namefile)



read_pdf = PyPDF2.PdfFileReader(pdf_file)

number_of_page = read_pdf.getNumPages( )

print ("PDF File has " + str(number_of_page) + " pages")
info = read_pdf.getDocumentInfo()
print info

#word = raw_input("What is the word to search in pdf file? : ")

pageview = 0

# kind of page pdf file of a page 
page = read_pdf.getPage(pageview)

page_number = read_pdf.getPageNumber(page)
print page_number

page_mode = read_pdf.getPageMode()
print page_mode

# extract_content of page 0

page_content = page.extractText()
print page_content.encode("latin-1")


