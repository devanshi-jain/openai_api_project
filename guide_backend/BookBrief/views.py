from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.core.files.base import ContentFile
import io
import PyPDF2

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def parse_pdf(request):
    if request.method == 'POST':
        # Get the uploaded file and page range from the form
        uploaded_file = request.FILES['pdf-file']
        page_range = request.POST.get('page-range')

        # Save the uploaded file to a temporary file on the server
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        uploaded_file_url = fs.url(filename)
        filepath = fs.path(filename)

        # Parse the PDF and get the summary for the selected page range
        with open(filepath, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            if page_range == 'all':
                text = ''
                for page in range(pdf_reader.numPages):
                    page_obj = pdf_reader.getPage(page)
                    text += page_obj.extractText()
            else:
                start, end = page_range.split('-')
                start = int(start) - 1
                end = int(end)
                text = ''
                for page in range(start, end):
                    page_obj = pdf_reader.getPage(page)
                    text += page_obj.extractText()

        # Render the summary as a string and return it as an HTTP response
        summary = render_to_string('summary.html', {'text': text})
        response = HttpResponse(summary, content_type='text/html')
        response['Content-Disposition'] = 'attachment; filename="summary.html"'
        return response

    else:
        return HttpResponse('Invalid request method')

