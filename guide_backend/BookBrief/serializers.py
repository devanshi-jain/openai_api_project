from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # fields = '__all__'
        fields = ['id', 'title', 'author', 'page_range', 'specified_page_range', 'pdf_file', 'uploaded_at']
