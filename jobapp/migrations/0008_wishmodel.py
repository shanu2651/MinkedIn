# Generated by Django 4.1.4 on 2023-01-28 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0007_alter_applymodel_resume_alter_userprofmodel_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='wishmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('jtitle', models.CharField(max_length=25)),
                ('jtype', models.CharField(max_length=25)),
                ('wtype', models.CharField(max_length=25)),
                ('exp', models.CharField(max_length=25)),
                ('qualify', models.CharField(max_length=70)),
            ],
        ),
    ]
