# Generated by Django 3.2.6 on 2021-11-03 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EncryptionScheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheme_name', models.CharField(max_length=200)),
                ('scheme_description', models.TextField(default='This is scheme')),
            ],
        ),
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('ids', models.AutoField(primary_key=True, serialize=False)),
                ('file_name', models.CharField(max_length=255)),
                ('file_data', models.FileField(upload_to='')),
                ('upload_type', models.CharField(choices=[('Encryption', 'Encryption'), ('Decryption', 'Decryption')], default='Encryption', max_length=50)),
                ('encryption_type', models.CharField(choices=[('NA', 'NA'), ('Caser', 'Caser'), ('AES (Advanced Encryption Standard) ', 'AES (Advanced Encryption Standard) '), ('One Time Pad', 'One Time Pad'), ('RSA Security', 'RSA Security'), ('Transposition Ciphers,', 'Transposition Ciphers,'), ('Vigenère cipher', 'Vigenère cipher')], default='NA', max_length=50)),
                ('decryption_type', models.CharField(choices=[('NA', 'NA'), ('Caser', 'Caser'), ('AES (Advanced Encryption Standard) ', 'AES (Advanced Encryption Standard) '), ('One Time Pad', 'One Time Pad'), ('RSA Security', 'RSA Security'), ('Transposition Ciphers,', 'Transposition Ciphers,'), ('Vigenère cipher', 'Vigenère cipher')], default='NA', max_length=50)),
                ('file_type', models.CharField(choices=[('Original', 'Original'), ('Encrypted', 'Encrypted'), ('Decrypted', 'Decrypted')], default='Original', max_length=50)),
                ('processed_file', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pair_file', to='app.fileupload')),
            ],
        ),
    ]
