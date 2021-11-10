from django.core.files.uploadedfile import UploadedFile
from django.db import models

from apps.Encrypt_Decrypt.one_time_pad_decryption import one_time_pad_decrytpion
from apps.Encrypt_Decrypt.one_time_pad_encryption import one_time_pad_encrytpion
from apps.Encrypt_Decrypt.vignere_decryption import vignere_decryption
from apps.Encrypt_Decrypt.vignere_encryption import vignere_encryption
from apps.app.models import FileUpload
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
    processed_file = FileUpload.objects.create()
    temp_file_name = models.CharField(max_length=255)
    temp_file_data =  models.FileField(upload_to='')



    def __init__(self, file_upload_obj):
        self.uploadedFile = file_upload_obj
        self.fileName = self.uploadedFile.getFileData().name
        self.fileData = self.uploadedFile.getFileData()
        print(self.fileName, self.fileData)
        print("we are in the Encryption Engine")

    def process_file(self):
        print('=========== indside process_file to choose encryption of decryption ============')
        print(self.uploadedFile.ids, self.uploadedFile.file_name, self.uploadedFile.file_data,
              self.uploadedFile.upload_type, self.uploadedFile.encryption_algorithms, self.uploadedFile.decryption_algorithms, self.uploadedFile.file_type)
        self.uploadedFile.processed_file = self.processed_file.processed_file
        if self.uploadedFile.upload_type == 'Encryption':
            self.encrypt()
        else:
            self.decrypt()

    def encrypt(self):
        print('=========== indside encrypt function ============')
        enctyption_type= self.uploadedFile.encryption_algorithms
        self.processed_file.file_type= 'Encrypted'
        self.processed_file.encryption_algorithms = self.uploadedFile.encryption_algorithms
        self.processed_file.file_name = "Encrypted_" + self.fileName

        # print(self.getInputFilePath())
        # print(self.getOutputFilePath())
        # print(enctyption_type)

        if enctyption_type== 'Vigenère cipher':
            print(enctyption_type)
            self.temp_upload_file_obj = vignere_encryption(self.getInputFilePath(), self.getOutputFilePath(), 'abc123')
            print( "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&" )
        elif enctyption_type == 'One Time Pad':
            print(enctyption_type)
            one_time_pad_encrytpion(self.getInputFilePath(),self.getOutputFilePath())

        elif enctyption_type == 'AES (Advanced Encryption Standard)':
            print(enctyption_type)

        elif enctyption_type == 'RSA Security':
            print(enctyption_type)

        self.updateProcessedFile()
        self.uploadedFile.processed_file=self.processed_file.processed_file

    def decrypt(self):
        print('=========== indside decryption function ============')
        dectyption_type= self.uploadedFile.decryption_algorithms
        self.processed_file.file_type= 'Decrypted'
        self.processed_file.decryption_algorithms = self.uploadedFile.decryption_algorithms
        self.processed_file.file_name = "Decrypted_" + self.fileName

        # print(self.getInputFilePath())
        # print(self.getOutputFilePath())
        # print(dectyption_type)

        if dectyption_type== 'Vigenère cipher':
            print(dectyption_type)
            self.processed_file.file_data.file= vignere_decryption(self.getInputFilePath(),self.getOutputFilePath(),'abc123')
        elif dectyption_type== 'One Time Pad':
            print(dectyption_type)
            self.processed_file.file_data.file= one_time_pad_decrytpion(self.getInputFilePath(),self.getOutputFilePath())

        elif dectyption_type == 'AES (Advanced Encryption Standard)':
            print(dectyption_type)

        elif dectyption_type == 'RSA Security':
            print(dectyption_type)

        self.updateProcessedFile()

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

    def updateProcessedFile(self):
        with open(self.getOutputFilePath(),'r') as self.processed_file.file_data:
            self.processed_file.file_data.read()

            print( self.getOutputFilePath())
            print(type(self.getOutputFilePath()))
            print(type(self.uploadedFile.file_data.url))
            print(self.uploadedFile.file_data.url)
            print(self.processed_file.file_data.read())
            # print("self.processed_file.file_data.file", self.processed_file.file_data.file)

            self.processed_file.setFileUrl(self.getOutputFilePath())
            if self.uploadedFile.upload_type == "Encryption":
                # self.processed_file.file_name = "Decrypted_" + self.fileName
                self.temp_file_name = "Encrypted_" + self.fileName
                processed_file = FileUpload.objects.create(file_name=self.temp_file_name, file_data=self.temp_file_data,
                                                           upload_type="Processed")

            else:
                self.temp_file_name = "Decrypted_" + self.fileName
                processed_file = FileUpload.objects.create(file_name=self.temp_file_name, file_data=self.temp_file_data,
                                                           upload_type="Processed")




        # with open(file_path, 'rb') as file:
        #     file_contents = file.read()
        #
        # # writing the file after decryption
        # with open(MEDIA_ROOT + "/Decrypted Files/Decrypted_" + self.fileName, 'wb') as file:
        #     file.write(file_contents)

