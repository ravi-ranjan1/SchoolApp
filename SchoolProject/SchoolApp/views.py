from django.shortcuts import render
from .models import Video_upload,Admission,Feedback,Exam_Upload,Questions
from .forms import Videoupload_form,SignUpForm,AdmissionForm,FeedbackForm,Exam_Upload_Form,Answer,Question_Form
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.conf import settings
from django.core.mail import send_mail
import csv
from django.contrib.auth.models import Group
from django.contrib import messages


# Create your views here.

def Home(request):
    request.session['name']='ravi'
    request.session.set_expiry(10)
    images=Video_upload.objects.values('Image')
    return render(request,'SchoolApp/Home.html',{'images':images})

@login_required(login_url='login')
def Img(request):
    return render(request,'SchoolApp/img.html')

@login_required(login_url='login')
def Upload(request):
    if request.method == 'POST':
        import ipdb
        ipdb.set_trace()
        form = Videoupload_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #return redirect('book_list')
    else:
        form = Videoupload_form()
    return render(request, 'SchoolApp/Video_Uploader.html', {
        'form': form
    })

@login_required(login_url='login')
def Exam_Upload_view(request):
    if request.method=='POST':
        form=Exam_Upload_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form=Exam_Upload_Form()
            csv_file=request.FILES['Question_file']
            for row in csv_file:
                    row=str(row).split(',')
                    created=Questions.objects.get_or_create(
                        Question=row[0],
                        Option1=row[1],
                        Option2=row[2],
                        Option3=row[3],
                        Option4=row[4],
                    )

    else:
        form=Exam_Upload_Form()
    return render(request,'SchoolApp/Question_Upload.html',{'form':form})

@login_required(login_url='login')
def Exam_View(request):
    # import ipdb
    # ipdb.set_trace()
    Exam_obj=Questions.objects.all()
    question_answer_obj = {}
    for e in Exam_obj:
        print('\n' * 3)
        print('post_data:', request.POST)
        print('\n' * 3)
        question_answer_obj[e.Question] = {0: e.Option1, 1: e.Option2, 2:e.Option3,3:e.Option4}

    import ipdb
    ipdb.set_trace()
    form = Question_Form()
    if request.method=='POST':
        post_data = request.POST
    else:
        return render(request,'SchoolApp/Exam.html',{'form1': question_answer_obj}, {'form': form})


@login_required(login_url='login')
def showvideo(request):
    data=Video_upload.objects.all()
    print (data)

    return render(request, 'SchoolApp/img.html',{'data':data})



@login_required(login_url='login')
def Docs(request):
    docs=Video_upload.objects.all()
    return render(request,'SchoolApp/Class2.html',{'docs':docs})


def Signup_view(request):

    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            username=form.cleaned_data.get('username')
            group=Group.objects.get(name='student')
            user.groups.add(group)
            messages.success(request,'Account is created for' + username)
            return HttpResponseRedirect('/')

    else:
        form=SignUpForm()
    return render(request,'SchoolApp/SignUp.html',{'form':form})


def Logout(request):
    return render(request,'SchoolApp/Logout.html')

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
def AdmissionCongrates(request):
    max_id = Admission.objects.get(Id=Admission.objects.aggregate(Max('Id')).get('Id__max'))
    fullDetails = Admission.objects.filter(Id=max_id.Id).values('Student_Name', 'Class_Name', 'RollNo')
    return render(request,'SchoolApp/AdmissionCOnfirmation.html',{'fullDetails':fullDetails})


