# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.app import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('encryption.html', views.upload_encryption, name='upload_files_en'),
    path('decryption.html', views.upload_decryption, name='upload_files_dec'),
    path('file-preview.html', views.file_preview, name='file_preview'),
    path('files-archive.html', views.files_archive, name='files_archive'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
