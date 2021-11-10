from django.db import models
from django.utils import timezone

import apps.app.models


class EncryptionScheme(models.Model):
    scheme_name = models.CharField(max_length=200)
    scheme_description = models.TextField(default='This is scheme')

    # pub_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.scheme_name


class FileUpload(models.Model):
    UPLOAD_CHOICES = (
        ('Encryption', 'Encryption'),
        ('Encryption', 'Encryption'),
        ('Processed', 'Processed')
    )

    FILE_TYPE = (
        ('Original', 'Original'),
        ('Encrypted', 'Encrypted'),
        ('Decrypted', 'Decrypted'),
    )

    ENCRYPTION_CHOICES = (
        ('NA', 'NA'),
        # ('Caser', 'Caser'),
        # ('Transposition Ciphers,', 'Transposition Ciphers,'),
        ('Vigenère cipher', 'Vigenère cipher'),
        ('One Time Pad', 'One Time Pad'),
        ('AES (Advanced Encryption Standard)', 'AES (Advanced Encryption Standard)'),
        ('RSA Security', 'RSA Security'),
    )

    ids = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=255)
    file_data = models.FileField(upload_to='')
    upload_type = models.CharField(max_length=50, choices=UPLOAD_CHOICES, default='Encryption')
    encryption_algorithms = models.CharField(max_length=50, choices=ENCRYPTION_CHOICES, default='NA')
    decryption_algorithms = models.CharField(max_length=50, choices=ENCRYPTION_CHOICES, default='NA')
    file_type = models.CharField(max_length=50, choices=FILE_TYPE, default='Original')
    processed_file = models.OneToOneField('self', null=True, blank=True, on_delete=models.CASCADE,
                                          related_name='pair_file')
    processed_file_name = models.CharField(max_length=255, default='none')
    processed_file_link = models.CharField(max_length=255, default='none 2')



    def __str__(self):
        return self.file_name

    def getFileName(self):
        return self.file_name

    def getFileData(self):
        return self.file_data

    def getUploadType(self):
        return self.upload_type

    def getEncryptionAlgorithms(self):
        return self.encryption_algorithms

    def getDecryptionAlgorithms(self):
        return self.decryption_algorithms

    def getFileType(self):
        return self.file_type

    def setFileUrl(self, url):
        self.file_data.url=url

    def getObj(self):
        return self
