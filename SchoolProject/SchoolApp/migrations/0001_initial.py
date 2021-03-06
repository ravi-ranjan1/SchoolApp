# Generated by Django 3.0.8 on 2020-07-31 11:23

from django.db import migrations, models
import django_google_maps.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Student_Name', models.CharField(max_length=100)),
                ('Class_Name', models.IntegerField()),
                ('Previous_School', models.CharField(max_length=100)),
                ('Father_Name', models.CharField(max_length=100)),
                ('Mother_Name', models.CharField(max_length=100)),
                ('Country', models.CharField(max_length=100)),
                ('State', models.CharField(choices=[('', 'Any'), ('BR', 'BIHAR'), ('UP', 'Uttar Pradesh'), ('MP', 'Madhya Pradesh')], max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('RollNo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AdmissionModel',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Student_Name', models.CharField(max_length=100)),
                ('Class_Name', models.IntegerField()),
                ('Previous_School', models.CharField(max_length=100)),
                ('Father_Name', models.CharField(max_length=100)),
                ('Mother_Name', models.CharField(max_length=100)),
                ('Country', models.CharField(max_length=100)),
                ('State', models.CharField(choices=[('', 'Any'), ('BR', 'BIHAR'), ('UP', 'Uttar Pradesh'), ('MP', 'Madhya Pradesh')], max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('RollNo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Subject', models.CharField(max_length=100)),
                ('Message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', django_google_maps.fields.AddressField(max_length=200)),
                ('geolocation', django_google_maps.fields.GeoLocationField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Video_upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('video_file', models.FileField(upload_to='videos/')),
                ('Image', models.ImageField(upload_to='Images/')),
                ('document', models.FileField(upload_to='Documents/')),
                ('created_date', models.DateTimeField(default='')),
            ],
        ),
    ]
