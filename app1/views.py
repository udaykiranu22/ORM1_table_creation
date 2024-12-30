from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app1.models import *

def insert_topic(request):
    tn = input('Enter a Topic Name : ')
    to = Topic.objects.get_or_create(Topic_name=tn)
    if to[1]:
        return HttpResponse(f'{tn} Data is added to Database.')
    else:
        return HttpResponse(f'{tn} Data is already in Database')

def insert_webpage(request):
    tn = input('Enter a Topic Name : ')
    n = input('Enter a Name : ')
    u = input('Enter a URL : ')
    to = Topic.objects.filter(Topic_name=tn)
    print(to)
    if to:
        wo = Webpage.objects.get_or_create(Topic_name=to[0], Name=n, Url=u)
        print(wo)
        if wo[1]:
            return HttpResponse(f'{n} Data is added to Database.')
        else:
            return HttpResponse(f'{n} Data is already in Database')
    else:
        return HttpResponse(f'{tn} Data is not in Database')

def insert_accessrecords(request):
    n = input('Enter a Name : ')
    a = input('Enter Author : ')
    d = input('Enter Date : ')
    wo = Webpage.objects.filter(Name=n)
    print(wo)
    if wo:
        ar = AccessRecords.objects.get_or_create(Name=wo[0], Author=a, Date=d)
        print(ar)
        if ar[1]:
            return HttpResponse(f'{a} Data is added to Database.')
        else:
            return HttpResponse(f'{a} Data is already in Database')
    else:
        return HttpResponse(f'{n} Data is not in Database')

def display_topic(request):
    topics = Topic.objects.all()
    d = {'topics': topics}
    return render(request, 'display_topic.html', d)

def display_webpage(request):
    webpage = Webpage.objects.all()
    d = {'webpage': webpage}
    return render(request, 'display_webpage.html', d)

def display_accessrecord(request):
    AR = AccessRecords.objects.all()
    d = {'AR': AR}
    return render(request, 'display_accessrecords.html', d)