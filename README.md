# Steps to get set up for this repository : 

Install require libraries by running the following code:
```
pip3 install python-dotenv
pip3 install openai
sudo pip install pipenv
pip3 install pdfminer
pip install pdfminer.six
pip3 install Django
pip3 install djangorestframework
from .serializers import BookSerializer
```

Create a '.env' file in your local branch, and add this line :
```
OPENAI_API_KEY = <your openai api key>
```

Add django to your path via : 
```
export PYTHONPATH=$PYTHONPATH:/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages
```
To set up the backend using Django, you can follow these general steps:

- Install Django by running ```pip install Django``` in your terminal.
- Create a new Django project using the command ```django-admin startproject <project_name>```.
- Create a new Django app using the command ```python manage.py startapp <app_name>```.
<!-- - Define the models you will use to store the PDF files and their corresponding metadata. You can use Django's built-in - models module to do this.
        # To create the corresponding database table for this model, you need to run the following commands:
        # python3 guide_backend/manage.py makemigrations
        # python3 guide_backend/manage.py migrate

- Create the necessary views to handle the REST API endpoints for uploading and retrieving PDF files and their metadata.
- Define the URLs for your views using Django's built-in urls module.
- Set up a database to store your PDF files and metadata. Django supports several database backends including SQLite, MySQL, and PostgreSQL. -->