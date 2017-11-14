from django.shortcuts import render
from django.http import HttpResponse
from appTwo.models import User
# Create your views here.

def index(request):
    return HttpResponse("<em>My Second Project</em>")

def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request,'appTwo/help.html',context=helpdict)

def users(request):
    users_list = User.objects.order_by('last_name')
    users_dict = {
        'access_users': users_list
    }
    return render(request,'appTwo/users.html', context=users_dict)
