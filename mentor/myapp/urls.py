from django.urls import path
from myapp.views import *

urlpatterns = [
    path('', home,name="H"),
    path('About/', about,name="A"),
    path('courses/',courses,name="C"),
    path('events/', events,name="E"),
    path('trainers/', trainers,name="T"),
    path('contact/', contact,name="co"),
    path('signup',signup,name='s' ),
    path('login',login,name='l' ),
]
