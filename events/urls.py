
from django.urls import path
from events.views import create_event,create_participant, update_category,create_category

urlpatterns = [
   path('create-event/', create_event, name='create-event'),
   path('create-participant/', create_participant, name='create-participant'),
   path('update-category/<id>/',update_category, name='update-category'),
   path('create-category/',create_category, name='create-category' )
]
