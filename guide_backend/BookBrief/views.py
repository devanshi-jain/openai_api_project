from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.core.files.base import ContentFile
import io
import PyPDF2

from pdf_parser import summarize_helper, get_completion

def index(request):
    return render(request, 'index.html')


def upload_book(request):
    if request.method == 'POST':
        # Get the uploaded file from the request
        uploaded_file = request.FILES['file']

        # Save the uploaded file to a temporary file on the server
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        uploaded_file_url = fs.url(filename)
        
        # Render a response with the URL of the uploaded file
        return render(request, 'upload_success.html', {'uploaded_file_url': uploaded_file_url})
    
    else:
        # Render a response with an upload form
        return render(request, 'upload.html')


def summarize(request):
    if request.method == 'POST':
        # Get the uploaded file and page range from the form
        uploaded_file = request.FILES['pdf-file']
        start_page = request.POST.get('start-page')
        end_page = request.POST.get('end-page')

        # Save the uploaded file to a temporary file on the server
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        uploaded_file_url = fs.url(filename)
        filepath = fs.path(filename)

        # Parse the PDF and get the summary for the selected page range
        with open(filepath, 'rb') as pdf_file:
            
            # pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            # if page_range == 'all':
            #     text = ''
            #     for page in range(pdf_reader.numPages):
            #         page_obj = pdf_reader.getPage(page)
            #         text += page_obj.extractText()
            # else:
            #     start, end = page_range.split('-')
            #     start = int(start) - 1
            #     end = int(end)
            #     text = ''
            #     for page in range(start, end):
            #         page_obj = pdf_reader.getPage(page)
            #         text += page_obj.extractText()
            summary = summarize_helper(pdf_file, start_page, end_page)

        # Render the summary as a string and return it as an HTTP response
        # summary = render_to_string('summary.html', {'text': text})
        response = HttpResponse(summary, content_type='text/html')
        response['Content-Disposition'] = 'attachment; filename="summary.html"'
        return response

    else:
        return HttpResponse('Invalid request method')

