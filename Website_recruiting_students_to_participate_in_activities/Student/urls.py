from django.urls import path
from Student.views import *

from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('',login_required(home,login_url="/login"), name='homeStudent'),
    path('activity/<int:id>/', activity),
    path('profileStudent', profileStudent, name='profileStudent'),
    path('updateprofileStudent/<int:id>/', updateprofileStudent, name='updateprofileStudent'),
]