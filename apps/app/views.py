
from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse

from .EncryptionEngine import EncryptionEngine
from .models import EncryptionScheme
from .forms import EncryptionForm, DecryptionForm
from .models import FileUpload
from django.db import models


def index(request):
    list_of_encryption_schemes = EncryptionScheme.objects.order_by('scheme_name')
    context = dict(list_of_encryption_schemes=list_of_encryption_schemes, segment='index')
    print(list_of_encryption_schemes)

    html_template = loader.get_template('index.html')
    return render(request, 'index.html', context)
    # return HttpResponse(html_template.render(context, request))


def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))


def upload_encryption(request):
    html_template = loader.get_template('encryption.html')

    if request.method == 'POST':
        form = EncryptionForm(request.POST, request.FILES)

        if form.is_valid():
            name = form.cleaned_data['file_name']
            the_files = form.cleaned_data['files_data']
            encryption_algorithms = form.cleaned_data['encryption_algorithms']

            uploaded_file = FileUpload.objects.create(file_name=name, file_data=the_files, encryption_algorithms=encryption_algorithms,  upload_type="Encryption")

            EncryptionEngine(uploaded_file).process_file()
            print(uploaded_file.file_data.file)
            print(uploaded_file.file_data.file)
            print(uploaded_file.file_data.name)
            print(uploaded_file.getFileName())


            return HttpResponse("<h1>File upload Successfully for Enctyption Check Project>core>media<h1>")
        else:
            return HttpResponse('Error in Uploading the file, form is not Valid')

    else:

        context = {
            'form': EncryptionForm()
        }

        # return HttpResponse(html_template.render(context, request))
        return render(request, 'encryption.html', context)


def upload_decryption(request):
    html_template = loader.get_template('decryption.html')

    if request.method == 'POST':
        form = DecryptionForm(request.POST, request.FILES)

        if form.is_valid():
            name = form.cleaned_data['file_name']
            the_files = form.cleaned_data['files_data']
            decryption_algorithms = form.cleaned_data['decryption_algorithms']

            # uploaded_file = FileUpload(file_name=name, file_data=the_files, decryption_type=decryption_type, upload_type="Decryption").save()
            uploaded_file = FileUpload.objects.create(file_name = name, file_data = the_files, decryption_algorithms = decryption_algorithms, upload_type="Decryption")
            EncryptionEngine(uploaded_file).process_file()

            return HttpResponse("<h1>File upload Successfully for Dectyption Check Project>core>media<h1>")
        else:
            return HttpResponse('Error in Uploading the file, form is not Valid')
    else:

        context = {
            'form': DecryptionForm()
        }

        # return HttpResponse(html_template.render(context, request))
        return render(request, 'decryption.html', context)


def files_archive(request):
    all_data = FileUpload.objects.all()

    context = {
        'data': all_data
    }

    return render(request, 'files-archive.html', context)

def file_preview(request):
    all_data = FileUpload.objects.all()

    context = {
        'data': all_data
    }

    return render(request, 'files-archive.html', context)