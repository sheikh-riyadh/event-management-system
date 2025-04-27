
from django.urls import path
from events.views import create_event,create_participant,create_category

urlpatterns = [
   path('create-event/', create_event, name='create-event'),
   path('create-participant/', create_participant, name='create-participant'),
   path('create-category/', create_category, name='create-category' )
]
