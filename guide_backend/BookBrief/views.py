from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

import io
from django.shortcuts import render
from django.http import JsonResponse



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