# Generated by Django 3.1 on 2020-08-10 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimage',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
