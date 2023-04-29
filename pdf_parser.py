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
        page_counter = -1
        if page_num is None:
            for page in PDFPage.get_pages(in_file, maxpages=0, caching=True, check_extractable=True):
                page_counter += 1
                interpreter.process_page(page)
                content = output_string.getvalue()
                text = f"""
                {content}
                """
                prompt = f"""
                Your task is to summarize pages of a book based on the content of the page provided.
                The page text is delimited by triple backticks.
                The summary is intended for someone trying to read the book on their own and need help understanding the content.
                It should be a short paragraph of 3-5 sentences.
                ```{content}```
                
                """
                response = get_completion(prompt)
                output_string.seek(0) #move cursor to beginning of file : 
                # ensures that subsequent calls to output_string.getvalue() start from the beginning of the string buffer
                output_string.truncate(0) #clear the string buffer so that it only contains the text parsed on the current page. 
                print(f'Page {page_num[page_counter]}:\n{response}')
        else:
            for page in PDFPage.get_pages(in_file, page_num, maxpages=0, caching=True, check_extractable=True):
                page_counter += 1
                interpreter.process_page(page)
                content = output_string.getvalue()
                output_string.seek(0)
                output_string.truncate(0)
                # print(f'The summary of Page {page_num[page_counter]}:\n{content}')
                text = f"""
                {content}
                """
                prompt = f"""
                Your task is to summarize pages of a book based on the content of the page provided.
                The page text is delimited by triple backticks.
                The summary is intended for someone trying to read the book on their own and need help understanding the content.
                It should be a short paragraph of 4-6 sentences.
                ```{content}```
                """
                response = get_completion(prompt)
                print(f'Page {page_num[page_counter]}:\n{response}')
    device.close()
    content = output_string.getvalue()
    output_string.close()
    return content

    
pdf_text = pdf_parse_text('The Subtle Art.pdf', [4,72])
print(pdf_text)