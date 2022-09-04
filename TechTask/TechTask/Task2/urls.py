from django.urls import path
from . import views

urlpatterns=[
    path('',views.Choose),
    path('1',views.Create),
    path('2',views.UpdateEvent),
    path('3',views.ViewEvents),
    path('4',views.DeleteEvents),
    path('5',views.DeleteAll),
]