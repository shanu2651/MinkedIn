# Generated by Django 4.1.4 on 2023-01-28 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0006_applymodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applymodel',
            name='resume',
            field=models.FileField(upload_to='jobapp/static'),
        ),
        migrations.AlterField(
            model_name='userprofmodel',
            name='image',
            field=models.ImageField(upload_to='jobapp/static'),
        ),
        migrations.AlterField(
            model_name='userprofmodel',
            name='resume',
            field=models.FileField(upload_to='jobapp/static'),
        ),
    ]
