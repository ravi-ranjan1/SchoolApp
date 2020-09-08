from django.db import models
from django_google_maps import fields as map_fields

# Create your models here.

class Video_upload(models.Model):
    Name=models.CharField(max_length=200)
    video_file=models.FileField(upload_to='videos/')
    Image=models.ImageField(upload_to='Images/')
    document=models.FileField(upload_to='Documents/')
    created_date=models.DateTimeField(default='')


class Rental(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)

STATE=(
    ('','Any'),
    ('BR','BIHAR'),
    ('UP','Uttar Pradesh'),
    ('MP','Madhya Pradesh')
)




class Feedback(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Subject=models.CharField(max_length=100)
    Message=models.TextField(max_length=1000)


class Admission(models.Model):
    Id=models.IntegerField(primary_key=True)
    Student_Name=models.CharField(max_length=100)
    Class_Name=models.IntegerField()
    Previous_School=models.CharField(max_length=100)
    Father_Name=models.CharField(max_length=100)
    Mother_Name=models.CharField(max_length=100)
    Country=models.CharField(max_length=100)
    State=models.CharField(choices=STATE,max_length=100)
    City=models.CharField(max_length=100)
    RollNo=models.IntegerField(null=True)

