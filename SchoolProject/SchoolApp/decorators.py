from django.http import HttpResponse
from django.shortcuts import redirect

def unathorized_user(view_fun):
    def wrapper_fun(request,*args,**kwargs):
        if request.user.is_authenticated:
            return ('/')
        else:
            return view_fun(request,*args,**kwargs)
