from http.client import HTTPResponse
from operator import mod
from sqlite3 import complete_statement
from django.shortcuts import render,redirect
from Task2.models import EventDet
from django.forms.models import model_to_dict
# Create your views here.

def Choose(request):
    choice=request.POST.get("CRUDchoice")
    if(choice):
        return redirect('/task2/{}'.format(choice))
    return render(request,"eve.html")

def Create(request):
    choice=request.POST.get("CRUDchoice")
    if(choice):
        return redirect('/task2/{}'.format(choice))

    name=request.POST.get("name")
    date=request.POST.get("date")
    desc=request.POST.get("des")
    completedEvent=request.POST.get("com")

    if(name and date and desc and completedEvent):
        e=EventDet()
        e.name=name
        e.date=date
        e.description=desc
        if(completedEvent=="on"):
            e.complete=True
        elif(completedEvent=="off"):
            e.complete=False
        e.save()
        return render(request,"eve.html",{'create':1,'created':1})

    return render(request,"eve.html",{'create':1})

def UpdateEvent(request):
    choice=request.POST.get("CRUDchoice")
    if(choice):
        return redirect('/task2/{}'.format(choice))
    return render(request,"eve.html")

def ViewEvents(request):
    choice=request.POST.get("CRUDchoice")
    if(choice):
        return redirect('/task2/{}'.format(choice))
    eventList=list()
    for e in EventDet.objects.all():
        eventList.append(model_to_dict(e))
    return render(request,"eve.html",{'view':1,'eventList':enumerate(eventList)})

def DeleteEvents(request):
    choice=request.POST.get("CRUDchoice")
    if(choice):
        return redirect('/task2/{}'.format(choice))
    return render(request,"eve.html")