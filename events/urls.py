
from django.urls import path
from events.views import create_event,create_participant

urlpatterns = [
   path('create-event/', create_event, name='event'),
   path('create-participant/', create_participant, name='participant')
]
