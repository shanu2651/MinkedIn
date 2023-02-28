from django.db import models

# Create your models here.
class regmodel(models.Model):
    cname=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    phone=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=12)
    cpassword=models.CharField(max_length=12)
class addmodel(models.Model):
    catchoice = [
        ('Part-Time','Part-Time'),
        ('Full-Time','Full-Time'),

    ]
    cho=[
        ('Hybrid','Hybrid'),
        ('Remote','Remote'),
    ]
    choice=[
        ('0-1','0-1'),
        ('1-2','1-2'),
        ('2-3','2-3'),
        ('3-4','3-4'),
        ('4-5','4-5'),
        ('5-6','5-6'),
        ('6-7','6-7'),
        ('7-8','7-8'),
        ('8-9','8-9'),
        ('9-10','9-10'),
    ]

    cname = models.CharField(max_length=50)
    email = models.EmailField()
    jtitle = models.CharField(max_length=25)
    jtype = models.CharField(max_length=25,choices=catchoice)
    wtype = models.CharField(max_length=25,choices=cho)
    exp = models.CharField(max_length=25,choices=choice)
    qualify = models.CharField(max_length=70)
class userprofmodel(models.Model):
    fullname=models.CharField(max_length=50)
    image=models.ImageField(upload_to='jobapp/static')
    email=models.EmailField()
    resume=models.FileField(upload_to='jobapp/static')
    eduquali=models.CharField(max_length=50)
    experience=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    phone=models.IntegerField()
class applymodel(models.Model):
    cname=models.CharField(max_length=25)
    jobtitle=models.CharField(max_length=50)
    fname=models.CharField(max_length=50)
    email=models.EmailField(max_length=30)
    resume=models.FileField(upload_to='jobapp/static')
class wishmodel(models.Model):
    cname = models.CharField(max_length=50)
    email = models.EmailField()
    jtitle = models.CharField(max_length=25)
    jtype = models.CharField(max_length=25)
    wtype = models.CharField(max_length=25)
    exp = models.CharField(max_length=25)
    qualify = models.CharField(max_length=70)



