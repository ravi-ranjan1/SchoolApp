from django import forms
from SchoolApp.models import Video_upload,Admission,Feedback
from django.contrib.auth.models import User

class Videoupload_form(forms.ModelForm):
    class Meta:
        model=Video_upload
        fields=["Name","video_file",'Image','document',"created_date"]



class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']

class AdmissionForm(forms.ModelForm):
    class Meta:
        model=Admission
        fields=['Student_Name','Class_Name' ,'Previous_School','Father_Name','Mother_Name' ,'Country','State','City']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields=['Name','Email','Subject','Message']
