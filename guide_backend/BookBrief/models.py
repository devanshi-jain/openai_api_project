from django.db import models

# Create your models here. You define a new model class with the fields you want to store.
# Each model class inherits from django.db.models.Model, the base class for all models.
# Define a Book model that inherits from Django's Model class

class Book(models.Model):
    # Define fields for the Book model
    class Meta:
        app_label = 'bookbrief'

    # - title: a CharField that can store up to 200 characters
    title = models.CharField(max_length=200)

    # - author: a CharField that can store up to 200 characters
    author = models.CharField(max_length=200)

    # - page_range: an IntegerField that stores the total number of pages in the book
    page_range = models.IntegerField()

     # - specified_page_range: a CharField that stores the user's specified page range in the format 'start-end'
    specified_page_range = models.CharField(max_length=200)

    # - pdf_file: a FileField that stores the uploaded PDF file and saves it to the 'pdfs/' directory
    pdf_file = models.FileField(upload_to='pdfs/')

    # - uploaded_at: a DateTimeField that automatically records the time when the book is uploaded
    uploaded_at = models.DateTimeField(auto_now_add=True)

    # Define a string representation for the Book model that returns the book's title
    def __str__(self):
        return self.title


# Object Relational Mapping (ORM) is a technique that lets you query and manipulate data from a database 
# using an object-oriented paradigm.

# Django uses ORM to map objects to database tables
# On defining a model class, Django automatically creates a database table for the model in the database
# MakeMigration command : create migrations files based on the changes made to the models
# Apply migration files to dB using the migrate command. 
# This creates the table in the dB and apply any changes to existing tables.

# RESULT :  Post running these commands, interact with the Book model in your views and templates. 
# ie create, read, update, and delete objects in the Book model through your Django application.

# To create the corresponding database table for this model, you need to run the following commands:
# python3 guide_backend/manage.py makemigrations
# python3 guide_backend/manage.py migrate






