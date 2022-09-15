from http.client import HTTPResponse
from django.shortcuts import render
import requests


# Create your views here.
def dog(request):
    allBreeds=requests.get('https://dog.ceo/api/breeds/list/all')
    if(allBreeds):
        allBreedDict=allBreeds.json()
        #print(allBreedDict["message"].keys())
    
    return render(request,"alldogs.html",{'alldogs':list(allBreedDict["message"].keys())})

def subdog(request,breed):
    subBreeds=requests.get('https://dog.ceo/api/breed/{}/list'.format(breed))
    subBreeds=subBreeds.json()
    print(subBreeds["message"])
    if(subBreeds["message"]==[]):
        subBreeds["message"]="No Sub Breeds"
    return render(request,"alldogs.html",{'sub':subBreeds["message"]})

def randomBreed(request):
    allBreeds=requests.get('https://dog.ceo/api/breeds/list/all')
    allBreeds=allBreeds.json()
    #indices=list()
    breeds=list(allBreeds["message"].keys())
    # for ind,name in enumerate(breeds):
    #     indices.append(ind)
    
    userInput=request.POST.get("breedChoice")
    if(userInput):
        im=requests.get('https://dog.ceo/api/breed/{}/images/random'.format(userInput))
        im=im.json()
        return render(request,"rand.html",{'breed':breeds,'image':im["message"],"bn":userInput})
    return render(request,"rand.html",{'breed':breeds})