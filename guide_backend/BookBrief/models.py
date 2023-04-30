from django.db import models

class Book(models.Model):
    # Define fields for the Book model
    class Meta:
        app_label = 'bookbrief'

    # - title: a CharField that can store up to 200 characters
    title = models.CharField(max_length=200)

    # - author: a CharField that can store up to 200 characters
    author = models.CharField(max_length=200)

    # - page_numbers: a CharField that stores the user's specified page range in the format 'start-end'
    page_numbers = models.CharField(max_length=200)

    # - pdf_file: a FileField that stores the uploaded PDF file and saves it to the 'pdfs/' directory
    pdf_file = models.FileField(upload_to='pdfs/')

    # - summary: a TextField that stores the summary of the book
    summary = models.TextField()

    # - uploaded_at: a DateTimeField that automatically records the time when the book is uploaded
    uploaded_at = models.DateTimeField(auto_now_add=True)

    # Define a string representation for the Book model that returns the book's title
    def __str__(self):
        return self.title
