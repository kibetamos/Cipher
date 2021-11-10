from django.contrib import admin

from .models import EncryptionScheme, FileUpload

admin.site.register(EncryptionScheme)
admin.site.register(FileUpload)
