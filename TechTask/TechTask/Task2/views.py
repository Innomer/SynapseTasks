from http.client import HTTPResponse
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

    if(name and date and desc):
        e=EventDet()
        e.name=name
        e.date=date
        e.description=desc
        if(completedEvent=="on"):
            e.complete=True
        else:
            e.complete=False
        e.save()
        return render(request,"eve.html",{'create':1,'created':1})

    return render(request,"eve.html",{'create':1})

def UpdateEvent(request):
    choice=request.POST.get("CRUDchoice")
    if(choice):
        return redirect('/task2/{}'.format(choice))
    eventList=list()
    for e in EventDet.objects.all():
        eventList.append(model_to_dict(e))
    delIndex=request.POST.get("UpdChoice")
    if(delIndex):
        for ind,n in enumerate(eventList):
            if(ind==int(delIndex)):
                e=EventDet.objects.filter(name=n['name'])
                for ev in e:
                    name=request.POST.get("name")
                    date=request.POST.get("date")
                    desc=request.POST.get("des")
                    completedEvent=request.POST.get("com")
                    print(name,date,desc,completedEvent)
                    if(name):
                        ev.name=name
                    if(date):
                        ev.date=date
                    if(desc):
                        ev.description=desc
                    if(completedEvent=="on"):
                        ev.complete=True
                    else:
                        ev.complete=False
                    ev.save()
        return render(request,"eve.html",{'update':1,'eventList':enumerate(eventList),'updated':1})    
    return render(request,"eve.html",{'update':1,'eventList':enumerate(eventList)})

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
    eventList=list()
    for e in EventDet.objects.all():
        eventList.append(model_to_dict(e))
    
    delIndex=request.POST.get("DelChoice")
    for ind,n in enumerate(eventList):
        if(ind==int(delIndex)):
            EventDet.objects.filter(name=n['name']).delete()
            return render(request,"eve.html",{'delete':1,'eventList':enumerate(eventList),'deleted':1})
    return render(request,"eve.html",{'delete':1,'eventList':enumerate(eventList)})

def DeleteAll(request):
    choice=request.POST.get("CRUDchoice")
    if(choice):
        return redirect('/task2/{}'.format(choice))
    EventDet.objects.filter(complete=True).delete()
    return render(request,"eve.html",{'delAll':1})