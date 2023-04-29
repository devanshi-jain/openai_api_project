# import re # regular expressions
# import openai_requests

# # Function to parse the TOC and return a dictionary of page numbers keyed by section titles
# def parse_toc(toc_text):
#     toc_lines = toc_text.split("\n")
#     toc_dict = {}
#     current_section = ""
#     for line in toc_lines:
#         # Check if the line is a section heading
#         if line.isupper() and line.endswith("..."):
#             current_section = line
#             toc_dict[current_section] = []
#         # Check if the line is a page number
#         elif line.isdigit():
#             toc_dict[current_section].append(int(line))
#     return toc_dict

# # Function to extract the table of contents (TOC) from the PDF text
# def extract_toc(pdf_text):
#     # capturing group to extract the TOC
#     # \s\S matches any whitespace character or any non-whitespace character
#     # *? matches the previous token between zero and unlimited times
#     # \n\d matches a newline character followed by a digit
#     toc_pattern = r"(Table of Contents|Contents)[\s\S]*?\n\d"
#     match = re.search(toc_pattern, pdf_text, re.IGNORECASE)
#     if match:
#         toc_text = match.group()
#         toc_dict = parse_toc(toc_text)
#         return toc_dict
#     else:
#         return None
    
# # Test the extract_toc function
# filename = 'The Subtle Art.pdf'
# pdf_text = extract_text(filename)
# toc = extract_toc(pdf_text)
# print(toc)


# # Function to correlate the PDF page numbers with the actual page numbers
# def correlate_page_numbers(pdf_page_numbers, toc_dict):
#     actual_page_numbers = []
#     for section_title, section_page_numbers in toc_dict.items():
#         for pdf_page_number in pdf_page_numbers:
#             if pdf_page_number in section_page_numbers:
#                 actual_page_numbers.append(section_page_numbers.index(pdf_page_number) + 1)
#     return actual_page_numbers
# Split the extracted text into sections based on headings
        # full_text = output_string.getvalue()
        # sections = []
        # current_section = ''
        # for line in full_text.split('\n'):
        #     if line.startswith('###'):
        #         sections.append(current_section)
        #         current_section = line[3:].strip() + '\n'
        #     else:
        #         current_section += line.strip() + '\n'
        # sections.append(current_section)
        
        # # Filter sections based on page numbers
        # sections = [section for i, section in enumerate(sections) if i+1 in page_nums]
        
        # # Clean up the text
        # sections = [section.strip() for section in sections if section.strip()]
        # title = title.strip() if title else None
        # author = author.strip() if author else None
        
        # return title, author, sections
        
    # filename = 'The Subtle Art.pdf'
    # page_nums = [2]

    # text = ""
    # # Open the PDF file in read-binary mode
    # with open(filename, 'rb') as file:
    #     # Create a PDF parser object
    #     parser = PDFParser(file)
    #     # Create a PDF document object
    #     document = PDFDocument(parser)
    #     # Get the metadata dictionary from the document information
    #     metadata = document.info[0]
    #     # Extract the title and author from the metadata dictionary
    #     title = metadata.get('Title', '')
    #     author = metadata.get('Author', '')
    #     # convert the title and author from byte string to unicode string
    #     title = title.decode()
    #     author = author.decode()

    #     # Create a PDF page aggregator object : extract text from specified pages
    #     laparams = LAParams()
    #     device = PDFPageAggregator(document, laparams=laparams)
    #     # Create a PDF interpreter object : interprets the text over the specified pages
    #     interpreter = PDFPageInterpreter(document, device)
        
    #     # Extract the text from all pages if actual_pages is None, or from specified pages
    #     if actual_pages is None:
    #         if toc_dict:
    #             pdf_page_numbers = list(range(1, document.catalog['Pages'].get('/Count', 0) + 1))
    #             actual_pages = correlate_page_numbers(pdf_page_numbers, toc_dict)
    #         else:
    #             actual_pages = list(range(1, document.catalog['Pages'].get('/Count', 0) + 1))
    #     else:
    #         if toc_dict:
    #             pdf_page_numbers = []
    #             for section_title, section_page_numbers in toc_dict.items():
    #                 for actual_page_number in actual_pages:
    #                     if actual_page_number in section_page_numbers:
    #                         pdf_page_numbers.append(section_page_numbers.index(actual_page_number) + 1)
    #             actual_pages = pdf_page_numbers
    #                         # Extract the text from the specified pages
    #     sections = []
    #     for page_number in actual_pages:
    #         interpreter.process_page(document.get_page(page_number))
    #         layout = device.get_result()
    #         for element in layout:
    #             if isinstance(element, (LTTextBox, LTTextLine)):
    #                 text = element.get_text().strip()
    #                 if text:
    #                     sections.append(text)
        # print(sections)
        # TODO : Write prompt and add text to print summary for each section
        # # Generate summaries for each section using OpenAI API
        # for section in sections:
        #     completion_text = get_completion(section)
        #     summary = completion_text["choices"][0]["text"].strip()
        #     print(summary)
#all extracted text from the specified pages, concatenated together.

# Example usage: extract text from pag

# # call the OpenAI API on each section
# for section in sections:
#     completion_text = get_completion(section)
#     print(completion_text)




    # response.choices is a list of possible completions generated by the model 
    # number of choices returned can be controlled by the "max_tokens" parameter
    # by deafult, max_tokens is set to 1 i.e. the highest scoring completion
    # .message contains the text of the completion
    # ["content"] is used to extract this text as a string
    # summary = response.choices[0].text.strip()

    # Note: response.choices[0] item also contains additional metadata about the generated completion like:
            # 1. log-likelihood score, 
            # 2. list of tokens representing the completion.