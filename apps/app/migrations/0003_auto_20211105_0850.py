# Generated by Django 3.2.6 on 2021-11-05 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211104_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupload',
            name='processed_file_link',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fileupload',
            name='processed_file_name',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='upload_type',
            field=models.CharField(choices=[('Encryption', 'Encryption'), ('Encryption', 'Encryption'), ('Processed', 'Processed')], default='Encryption', max_length=50),
        ),
    ]
