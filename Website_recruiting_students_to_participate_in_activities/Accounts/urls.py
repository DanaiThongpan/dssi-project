from django.urls import path, include
from Accounts.views import home, login, Register, RegisterPerson_responsible_for_the_project, logout
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('Register/', Register, name='Register'),
    # path('RegisterStudent/', RegisterStudent, name='RegisterStudent'),
    path('RegisterPerson_responsible_for_the_project/', RegisterPerson_responsible_for_the_project,name='RegisterPerson_responsible_for_the_project'),
    path('logout/', logout, name='logout'),
]