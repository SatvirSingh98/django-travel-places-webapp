# Generated by Django 3.0.6 on 2020-05-11 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0002_auto_20200511_0715'),
    ]

    operations = [
        migrations.AddField(
            model_name='description',
            name='name',
            field=models.CharField(default=True, max_length=100),
            preserve_default=False,
        ),
    ]
