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
        page_counter = 0
        if page_num is None:
            for page in PDFPage.get_pages(in_file, maxpages=0, caching=True, check_extractable=True):
                page_counter += 1
                interpreter.process_page(page)
                content = output_string.getvalue()
                output_string.seek(0) #move cursor to beginning of file : 
                # ensures that subsequent calls to output_string.getvalue() start from the beginning of the string buffer
                output_string.truncate(0) #clear the string buffer so that it only contains the text parsed on the current page. 
                print(f'Page {page_num[page_counter]}:\n{content}')
        else:
            for page in PDFPage.get_pages(in_file, page_num, maxpages=0, caching=True, check_extractable=True):
                interpreter.process_page(page)
                content = output_string.getvalue()
                output_string.seek(0)
                output_string.truncate(0)
                print(f'The summary of Page {page_num[page_counter]}:\n{content}')
    device.close()
    content = output_string.getvalue()
    output_string.close()
    return content



        # TODO : Write prompt and add text to print summary for each section
        # Generate summaries for each section using OpenAI API
        # for section in sections:
        #     completion_text = get_completion(section)
        #     summary = completion_text["choices"][0]["text"].strip()
        #     print(summary)
        
pdf_text = pdf_parse_text('The Subtle Art.pdf', [72])
# toc = extract_toc(pdf_text)
print(pdf_text)