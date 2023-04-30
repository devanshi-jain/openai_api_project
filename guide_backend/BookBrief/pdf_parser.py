# Authorization: Bearer OPENAI_API_KEY

# /////////////////////////////////SETUP////////////////////////////////////////
import openai
import os
import re

# import necessary libraries
from dotenv import load_dotenv
from io import StringIO
from pdfminer.layout import LAParams
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams, LTTextBox, LTTextLine
from pdfminer.converter import PDFPageAggregator, TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager

# from prompt_iteration import get_completion

# Load environment variables from .env file
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) #reads local .env file

# Get value of OPENAI_API_KEY environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")

# Set the API key for the OpenAI API client
openai.api_key = openai_api_key

# function uses the OpenAI API client to generate text based on a prompt using 
def get_completion(prompt, model="gpt-3.5-turbo"):
    # user prompt (initialized as a list)
    # 2 key-value pairs: role (indicates message is from 'user') and content.
    messages = [{"role": "user", "content": prompt}]
    # response from the api call
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=256,
        temperature=0, # degree of randomness of the model's output
        n = 1 # number of completions to generate for each prompt
    )
    return response.choices[0].message["content"]

def pdf_parse_text(file, start_page=None, end_page=None):
    output_string = StringIO()
    with file as in_file:
        resource_manager = PDFResourceManager()
        device = TextConverter(resource_manager, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(resource_manager, device)
        parser = PDFParser(in_file)
        document = PDFDocument(parser)
        metadata = document.info[0]
        title = metadata.get('Title', '')
        author = metadata.get('Author', '')
        for page_number, page in enumerate(PDFPage.get_pages(in_file, maxpages=0, caching=True, check_extractable=True), start=1):
            if start_page is not None and page_number < start_page:
                continue
            if end_page is not None and page_number > end_page:
                break
            interpreter.process_page(page)
            content = output_string.getvalue()
            output_string.seek(0)
            output_string.truncate(0)
            prompt = f"""
            Your task is to summarize pages of a book based on the content of the page provided.
            The page text is delimited by triple backticks.
            The summary is intended for someone trying to read the book on their own and need help understanding the content.
            It should be a short paragraph of 4-6 sentences.
            ```{content}```
            """
            response = get_completion(prompt)
            yield response
    device.close()
    output_string.close()

    #         response = get_completion(prompt)
#         print(f'Page {page_num[page_counter]}:\n{response}')
#     device.close()
#     content = output_string.getvalue()
#     output_string.close()
#     return content
# Function that takes a filename and a list of page numbers and returns the extracted summary from the PDF for those pages
# def pdf_parse_text(file_path, page_num=None):
#     output_string = StringIO()
#     with open(file_path, 'rb') as in_file:
#         resource_manager = PDFResourceManager()
#         device = TextConverter(resource_manager, output_string, laparams=LAParams())
#         interpreter = PDFPageInterpreter(resource_manager, device)
#         # Get the PDF document information
#         parser = PDFParser(in_file)
#         document = PDFDocument(parser)
#         metadata = document.info[0]
#         # Extract the title and author from the metadata dictionary
#         title = metadata.get('Title', '') #.decode() #TODO : add conditional block to check for by Author.
#         author = metadata.get('Author', '') #.decode()
#         # Print the title and author
#         print(f'Title: {title}\nAuthor: {author}')
#         page_counter = -1
#     for page in PDFPage.get_pages(in_file, page_num, maxpages=0, caching=True, check_extractable=True):
#         page_counter += 1
#         interpreter.process_page(page)
#         content = output_string.getvalue()
#         output_string.seek(0)
#         output_string.truncate(0)
#         # print(f'The summary of Page {page_num[page_counter]}:\n{content}')
#         text = f"""
#         {content}
#         """
#         prompt = f"""
#         Your task is to summarize pages of a book based on the content of the page provided.
#         The page text is delimited by triple backticks.
#         The summary is intended for someone trying to read the book on their own and need help understanding the content.
#         It should be a short paragraph of 4-6 sentences.
#         ```{content}```
#         """
#         response = get_completion(prompt)
#         print(f'Page {page_num[page_counter]}:\n{response}')
#     device.close()
#     content = output_string.getvalue()
#     output_string.close()
#     return content


pdf_text = pdf_parse_text('the-aeneid.pdf',83, 83)
print(pdf_text)