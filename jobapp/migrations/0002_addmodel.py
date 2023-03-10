# Generated by Django 4.1.4 on 2023-01-06 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='addmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('jtitle', models.CharField(max_length=25)),
                ('jtype', models.CharField(choices=[('Part-Time', 'Part-Time'), ('Full-Time', 'Full-Time')], max_length=25)),
                ('wtype', models.CharField(choices=[('Hybrid', 'Hybrid'), ('Remote', 'Remote')], max_length=25)),
                ('exp', models.CharField(choices=[('0-1', '0-1'), ('1-2', '1-2'), ('2-3', '2-3'), ('3-4', '3-4'), ('4-5', '4-5'), ('5-6', '5-6'), ('6-7', '6-7'), ('7-8', '7-8'), ('8-9', '8-9'), ('9-10', '9-10')], max_length=25)),
                ('qualify', models.CharField(max_length=70)),
            ],
        ),
    ]
