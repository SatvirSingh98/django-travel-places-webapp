# Generated by Django 3.0.6 on 2020-05-11 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0003_description_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.DeleteModel(
            name='Description',
        ),
    ]
