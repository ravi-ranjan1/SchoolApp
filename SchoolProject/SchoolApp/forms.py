from django import forms
from SchoolApp.models import Video_upload,Admission,Feedback,Exam_Upload,Questions,Answer
from django.contrib.auth.models import User
from django.core import validators

class Videoupload_form(forms.ModelForm):
    class Meta:
        model=Video_upload
        fields=["Name","video_file",'Image','document',"created_date"]




class SignUpForm(forms.ModelForm):
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['username','password','confirm_password','email','first_name','last_name']

    def clean(self):
        super(SignUpForm,self).clean()

        password=self.cleaned_data.get('password')
        if len(password) < 8:
            self._errors['password']=self.error_class(['The password must be at least 8 charecters'])
        elif len(password) >= 8:
             if password[0:3].isalpha() and password[3:5].isnumeric() and password[5:] in '~!@#$%^&*':
                 print('ok')
             else:
                 self._errors['password']=self.error_class(['The password must contain-->first 3 charecters albahbetic , next 2 charecters numeric and rest should be special charecters.'])
        confirm_password=self.cleaned_data.get('confirm_password')
        if password!=confirm_password:
            self._errors['confirm_password']=self.error_class(['Password didn\'t match.Please re-enter the password!'])

class AdmissionForm(forms.ModelForm):
    class Meta:
        model=Admission
        fields=['Student_Name','Class_Name' ,'Previous_School','Father_Name','Mother_Name' ,'Country','State','City']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields=['Name','Email','Subject','Message']


class Exam_Upload_Form(forms.ModelForm):
    class Meta:
        model=Exam_Upload
        fields=['Question_file']


ANSWER_CHOICES = (
    (1, 'choice 1'),
    (2, 'choice 2'),
    (3, 'choice 3'),
    (4, 'choice 4'),
)

class Question_Form(forms.ModelForm):
    Question = forms.CharField(max_length=200)

    Answer = forms.ChoiceField(choices=ANSWER_CHOICES, required=True,
                                     widget=forms.RadioSelect(
                                         attrs={'class': 'radio', 'type': 'radio', 'required': True}))

    class Meta:
        model=Questions
        fields=['Question','Option1','Option2','Option3','Option4']



