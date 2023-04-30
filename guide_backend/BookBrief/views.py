from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Create your views here.
# Views in Django are functions that take an HTTP request and return an HTTP response.
# They define how the application handles various HTTP requests. 

# Want to create views to handle the REST API endpoints for uploading and retrieving PDF files and their metadata.

# We need two views:
# - "UploadBookView" : handles the POST request for uploading a PDF file and its metadata, and saves the file to the database
# - "GetBookView" : handles the GET request for retrieving the PDF file and its metadata from the database