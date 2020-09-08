from django.contrib import admin
from SchoolApp.models import Video_upload,Admission,Feedback
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

