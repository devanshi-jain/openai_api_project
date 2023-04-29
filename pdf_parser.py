from io import StringIO
import os
import re # regular expressions

# import necessary libraries
# from pdfminer.high_level import extract_text
from pdfminer.layout import LAParams
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams, LTTextBox, LTTextLine
from pdfminer.converter import PDFPageAggregator, TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager

from prompt_iteration import get_completion

# Function that takes a filename and a list of page numbers and returns the extracted text from the PDF for those pages
def pdf_parse_text(file_path, page_num=None):
    output_string = StringIO()
    with open(file_path, 'rb') as in_file:
        resource_manager = PDFResourceManager()
        device = TextConverter(resource_manager, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(resource_manager, device)
        title = ''
        author = ''
        if page_num is None:
            for page in PDFPage.get_pages(in_file, maxpages=0, caching=True, check_extractable=True):
                interpreter.process_page(page)
        else:
            for page in PDFPage.get_pages(in_file, page_num, maxpages=0, caching=True, check_extractable=True):
                interpreter.process_page(page)
        device.close()
    content = output_string.getvalue()
    output_string.close()
    return content
        
pdf_text = pdf_parse_text('The Subtle Art.pdf', [72])
# toc = extract_toc(pdf_text)
print(pdf_text)