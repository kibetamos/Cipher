from django import forms
from .models import FileUpload


class EncryptionForm(forms.Form):
    # class Meta:
    #     model = file_upload
    #     fields = ['file_name', 'file_data', 'upload_type', 'encryption_type', 'decryption_type']

    encryption_algorithms = forms.ChoiceField(choices=FileUpload.ENCRYPTION_CHOICES)
    # decryption_type = forms.ChoiceField(choices=file_upload.ENCRYPTION_CHOICES)
    file_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    files_data = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))


class DecryptionForm(forms.Form):

    # encryption_type = forms.ChoiceField(choices=file_upload.ENCRYPTION_CHOICES)
    decryption_algorithms = forms.ChoiceField(choices=FileUpload.ENCRYPTION_CHOICES)
    file_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    files_data = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))
