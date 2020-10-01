from django.contrib import admin
from SchoolApp.models import Video_upload,Admission,Feedback,Exam,Exam_Upload,Questions
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

# Register your models here.
class VideoAdmin(admin.ModelAdmin):
    list_display = ['Name','video_file','Image','document','created_date']
admin.site.register(Video_upload,VideoAdmin)

class RentalAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {
          'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
    }



class AdmissionAdm(admin.ModelAdmin):
    list_display = ['Id','Student_Name','Class_Name' ,'Previous_School','Father_Name','Mother_Name' ,'Country','State','City','RollNo']
admin.site.register(Admission,AdmissionAdm)


class FeedbackAdm(admin.ModelAdmin):
    list_display =['Name','Email','Subject','Message']
admin.site.register(Feedback,FeedbackAdm)

class ExamAdmin(admin.ModelAdmin):
    list_display = ['Id','Student_Name','Question','Answer']
admin.site.register(Exam,ExamAdmin)

class Exam_UploadAdmin(admin.ModelAdmin):
    list_display = ['Id','Question_file']
admin.site.register(Exam_Upload,Exam_UploadAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['Question','Option1','Option2','Option3','Option4']
admin.site.register(Questions,QuestionAdmin)

# class AnswersAdmin(admin.ModelAdmin):
#     list_display = ['Id','Answer']
# admin.site.register(AdmissionAdm,AnswersAdmin)


