from django.urls import path
from Person_responsible_for_the_project.views import *

urlpatterns = [
    path('',home, name='home'),
    path('profilePerson_responsible_for_the_project', profilePerson_responsible_for_the_project, name='profilePerson_responsible_for_the_project'),
    path('updateprofilePerson_responsible_for_the_project/<int:id>/', updateprofilePerson_responsible_for_the_project, name='updateprofilePerson_responsible_for_the_project'),
    path('create_activity2/', create_activity2, name='create_activity2'),
    path('activity_crateby_user2/update_activity/<int:id>/', update_activity2, name="update_activity2"),
    path('activity_crateby_user2/', activity_crateby_user2, name='activity_crateby_user2'),
]
