from django.shortcuts import render
# from rest_framework import generics, status
# from rest_framework.response import Response
# from .models import Book
# from .serializers import BookSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from io import BytesIO
import PyPDF2
from PyPDF2 import PdfFileReader

import sys
# sys.path.append('/path/to/myproject')
from BookBrief.pdf_parser import pdf_parse_text
# from guide_backend.BookBrief.pdf_parser import pdf_parse_text


@csrf_exempt
def summarize_pdf(request):
    if request.method == 'POST':
        # Get the uploaded file
        uploaded_file = request.FILES['pdf_file']
        # Read the PDF file from the buffer
        pdf_reader = PdfFileReader(BytesIO(uploaded_file.read()))
        # Get the total number of pages in the PDF file
        total_pages = pdf_reader.getNumPages()
        # Get the page numbers to parse
        page_numbers = request.POST.getlist('page_numbers[]')
        # Convert the page numbers to integers
        page_numbers = [int(p) for p in page_numbers]
        # Filter the page numbers that are greater than the total number of pages
        page_numbers = [p for p in page_numbers if p <= total_pages]
        # Call the pdf_parse_text function to get the summary of the specified pages
        summary = pdf_parse_text(uploaded_file, page_numbers)
        # Return the summary as the response
        return HttpResponse(summary)
    else:
        # Return a 405 error if the request method is not POST
        return HttpResponse('Method Not Allowed', status=405)


# from PyPDF2 import PdfFileReader
# from .forms import PDFUploadForm

# def parse_pdf(request):
#     if request.method == 'POST':
#         form = PDFUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             # Get the uploaded PDF file and page numbers
#             pdf_file = form.cleaned_data['pdf_file']
#             page_numbers = form.cleaned_data['page_numbers']
            
#             # Parse the PDF file and extract text
#             pdf_reader = PdfFileReader(io.BytesIO(pdf_file.read()))
#             if page_numbers == 'all':
#                 page_range = range(pdf_reader.getNumPages())
#             else:
#                 start_page, end_page = page_numbers.split('-')
#                 page_range = range(int(start_page) - 1, int(end_page))
#             text = ''
#             for i in page_range:
#                 text += pdf_reader.getPage(i).extractText()
            
#             # Return the extracted text as a JSON response
#             return JsonResponse({'text': text})
#     else:
#         form = PDFUploadForm()
    
#     return render(request, 'index.html', {'form': form})


# class BookListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# Views in Django are functions that take an HTTP request and return an HTTP response.
# They define how the application handles various HTTP requests. 

# Want to create views to handle the REST API endpoints for uploading and retrieving PDF files and their metadata.

# We need two views:
# - "UploadBookView" : handles the POST request for uploading a PDF file and its metadata, and saves the file to the database
# - "GetBookView" : handles the GET request for retrieving the PDF file and its metadata from the database