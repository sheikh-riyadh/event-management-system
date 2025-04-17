
from django.urls import path
from events.views import create_event,create_participant, update_category,dashboard

urlpatterns = [
   path('create-event/', create_event, name='event'),
   path('create-participant/', create_participant, name='participant'),
   path('update-category/<int:id>/',update_category, name="update-category"),
   path('dashboard/', dashboard, name='dashboard')
]
