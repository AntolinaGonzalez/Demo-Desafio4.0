# Generated by Django 3.1 on 2020-08-10 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageToCompare', models.ImageField(upload_to='images')),
                ('imageTarget', models.ImageField(upload_to='images')),
                ('objetivo', models.CharField(max_length=150)),
                ('created_document_timestamp', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
