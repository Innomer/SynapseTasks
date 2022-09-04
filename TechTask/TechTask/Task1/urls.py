from django.urls import path
from . import views
urlpatterns=[
    path('allDogs',views.dog),
    path('subDogs/<str:breed>',views.subdog),
    path('random/',views.randomBreed),
]