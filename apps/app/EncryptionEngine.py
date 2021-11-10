from django.core.files.uploadedfile import UploadedFile
from django.db import models
from django.core.files.uploadhandler import FileUploadHandler,InMemoryUploadedFile,TemporaryFileUploadHandler

from apps.Encrypt_Decrypt.one_time_pad_decryption import one_time_pad_decrytpion
from apps.Encrypt_Decrypt.one_time_pad_encryption import one_time_pad_encrytpion
from apps.Encrypt_Decrypt.vignere_decryption import vignere_decryption
from apps.Encrypt_Decrypt.vignere_encryption import vignere_encryption
from apps.app.models import FileUpload
from django.core.files import File
import os
from os import path
from unipath import Path

from core.settings import MEDIA_ROOT


# ids = models.AutoField(primary_key=True)
# file_name = models.CharField(max_length=255)
# file_data = models.FileField(upload_to='')
# encryption_algorithms = models.CharField(max_length=50, choices=ENCRYPTION_CHOICES, default='NA')
# decryption_algorithms = models.CharField(max_length=50, choices=ENCRYPTION_CHOICES, default='NA')
# file_type = models.CharField(max_length=50, choices=FILE_TYPE, default='Original')


class EncryptionEngine:
    # processed_file = FileUpload.objects.create()
    temp_file_name = ''
    temp_file_data = models.FileField(upload_to='')
    temp_file_type = ''
    decryption_algorithms = ''
    encryption_algorithms = ''
    upload_handeler = FileUploadHandler()

    def __init__(self, file_upload_obj):
        self.uploadedFile = file_upload_obj
        self.fileName = self.uploadedFile.getFileData().name
        self.fileData = self.uploadedFile.getFileData()
        print(self.fileName, self.fileData)
        print("we are in the Encryption Engine")

    def process_file(self):
        print('=========== indside process_file to choose encryption of decryption ============')
        print(self.uploadedFile.ids, self.uploadedFile.file_name, self.uploadedFile.file_data,
              self.uploadedFile.upload_type, self.uploadedFile.encryption_algorithms,
              self.uploadedFile.decryption_algorithms, self.uploadedFile.file_type)
        if self.uploadedFile.upload_type == 'Encryption':
            self.encrypt()
        else:
            self.decrypt()
        # self.updateProcessedFile()
        self.uploadedFile.processed_file_name = self.updateProcessessedFileName()
        self.uploadedFile.processed_file_link = self.updateProcessessedFileLink()
        self.uploadedFile.save()
        print("Just Saved our Uploaded File Object")
    def encrypt(self):
        print('=========== indside encrypt function ============')
        enctyption_type = self.uploadedFile.encryption_algorithms

        # print(self.getInputFilePath())
        # print(self.getOutputFilePath())
        # print(enctyption_type)

        if enctyption_type == 'Vigenère cipher':
            print(enctyption_type)
            vignere_encryption(self.getInputFilePath(), self.getOutputFilePath(), 'abc123')
            print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        elif enctyption_type == 'One Time Pad':
            print(enctyption_type)
            one_time_pad_encrytpion(self.getInputFilePath(), self.getOutputFilePath())

        elif enctyption_type == 'AES (Advanced Encryption Standard)':
            print(enctyption_type)

        elif enctyption_type == 'RSA Security':
            print(enctyption_type)



    def decrypt(self):
        print('=========== indside decryption function ============')
        dectyption_type = self.uploadedFile.decryption_algorithms

        # print(self.getInputFilePath())
        # print(self.getOutputFilePath())
        # print(dectyption_type)

        if dectyption_type == 'Vigenère cipher':
            print(dectyption_type)
            vignere_decryption(self.getInputFilePath(), self.getOutputFilePath(), 'abc123')

        elif dectyption_type == 'One Time Pad':
            print(dectyption_type)
            one_time_pad_decrytpion(self.getInputFilePath(), self.getOutputFilePath())

        elif dectyption_type == 'AES (Advanced Encryption Standard)':
            print(dectyption_type)

        elif dectyption_type == 'RSA Security':
            print(dectyption_type)

    def getInputFilePath(self):
        file_path = os.path.join(MEDIA_ROOT, self.fileName)
        return file_path

    def getOutputFilePath(self):
        file_path = ''
        if self.uploadedFile.upload_type == 'Encryption':
            file_path = MEDIA_ROOT + "/Encrypted Files/Encrypted_" + self.fileName
        else:
            file_path = MEDIA_ROOT + "/Decrypted Files/Decrypted_" + self.fileName
        print(file_path)
        return file_path


    def updateProcessessedFileLink(self):

        if self.uploadedFile.upload_type == 'Encryption':
            file_link ="http://127.0.0.1:8000/media/Encrypted Files/Encrypted_" + self.fileName
        else:
            file_link ="http://127.0.0.1:8000/media/Decrypted Files/Decrypted_" + self.fileName
        return file_link



    def updateProcessessedFileName(self):

        if self.uploadedFile.upload_type == 'Encryption':
            file_name ="Encrypted_" + self.fileName
        else:
            file_name ="Decrypted_" + self.fileName
        return file_name



    def updateProcessedFile(self):
        # file_obj = open(self.getOutputFilePath(), 'rb').read()
        self.temp_file_data = File(name=self.temp_file_name, file=open(self.getOutputFilePath(), 'rb').read())

        # print("self.processed_file.file_data.file", self.processed_file.file_data.file)

        if self.uploadedFile.upload_type == "Encryption":
            # self.processed_file.file_name = "Decrypted_" + self.fileName
            self.temp_file_name = "Encrypted_" + self.fileName
            self.encryption_algorithms = self.uploadedFile.encryption_algorithms
            processed_file = FileUpload.objects.create(file_name=  self.temp_file_name, file_data=self.temp_file_data,
                                                       upload_type="Processed",
                                                       encryption_algorithms=self.encryption_algorithms,
                                                       file_type="Encrypted")
            # processed_file.setFileUrl(self.getOutputFilePath())
            self.uploadedFile.processed_file = processed_file.processed_file
            # file_obj.close()
            processed_file.save()

        else:
            self.temp_file_name = "Decrypted_" + self.fileName
            self.decryption_algorithms = self.uploadedFile.decryption_algorithms
            processed_file = FileUpload.objects.create(file_name = self.temp_file_name, file_data=self.temp_file_data,
                                                       upload_type="Processed",
                                                       decryption_algorithms=self.decryption_algorithms,
                                                       file_type="Decrypted")
            # processed_file.setFileUrl(self.getOutputFilePath())
            self.uploadedFile.processed_file = processed_file.processed_file
            processed_file.save()

    # with open(file_path, 'rb') as file:
    #     file_contents = file.read()
    #
    # # writing the file after decryption
    # with open(MEDIA_ROOT + "/Decrypted Files/Decrypted_" + self.fileName, 'wb') as file:
    #     file.write(file_contents)
