from django.shortcuts import render
from .models import Video_upload,Admission,Feedback
from .forms import Videoupload_form,SignUpForm,AdmissionForm,FeedbackForm
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def Home(request):
    return render(request,'SchoolApp/Home.html')


def Img(request):
    return render(request,'SchoolApp/img.html')

def Upload(request):
    if request.method == 'POST':
        form = Videoupload_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #return redirect('book_list')
            print ''
    else:
        form = Videoupload_form()
    return render(request, 'SchoolApp/Video_Uploader.html', {
        'form': form
    })



def showvideo(request):
    data=Video_upload.objects.filter(Image__contains='Moto')
    print (data)

    return render(request, 'SchoolApp/img.html',{'data':data})

def Docs(request):
    docs=Video_upload.objects.all()
    return render(request,'SchoolApp/Class2.html',{'docs':docs})

def Signup_view(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else:
        form=SignUpForm()
    return render(request,'SchoolApp/SignUp.html',{'form':form})

def Logout(request):
    return render(request,'SchoolApp/Logout.html')

def Contact(request):
    if request.method=='POST':
        form=FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            Max_id=Feedback.objects.latest('id').id
            Data=Feedback.objects.values('Name','Email','Subject','Message').filter(id=Max_id)
            Name=Data[0]['Name']
            Subject=Data[0]['Subject']
            Email=[Data[0]['Email'],]
            Message=Data[0]['Message']
            email_from=settings.EMAIL_HOST_USER
            send_mail(Subject,Message,email_from,Email)


            return HttpResponseRedirect('/')
    else:
        form=FeedbackForm()
    return render(request,'SchoolApp/Contact.html',{'form':form})


def AdmissionView(request):
    if request.method=='POST':
        form=AdmissionForm(request.POST)
        if form.is_valid():

            form.save()
            max_id=Admission.objects.get(Id=Admission.objects.aggregate(Max('Id')).get('Id__max'))
            rollno = Admission.objects.get(RollNo=Admission.objects.aggregate(Max('RollNo')).get('RollNo__max'))
            max_id.RollNo=rollno.RollNo+1
            max_id.save()
            Name=Admission.objects.values_list('Student_Name').filter(RollNo=max_id.RollNo)
            subject='Admission Confirmed'
            message='Congratulations '+str(Name[0][0])+' ! Your Admission is confirmed. '+str(max_id.RollNo)+' roll number is alloted to You.'
            email_from=settings.EMAIL_HOST_USER
            recipient_list=['44ravi.ranjan@gmail.com',]
            send_mail(subject,message,email_from,recipient_list)


            return HttpResponseRedirect('/AdmissionConfirmation')
    else:
        form=AdmissionForm()
        context={'form':form}
        return render(request,'SchoolApp/Admission.html',context)

def AdmissionCongrates(request):
    max_id = Admission.objects.get(Id=Admission.objects.aggregate(Max('Id')).get('Id__max'))
    fullDetails = Admission.objects.filter(Id=max_id.Id).values('Student_Name', 'Class_Name', 'RollNo')
    return render(request,'SchoolApp/AdmissionCOnfirmation.html',{'fullDetails':fullDetails})


