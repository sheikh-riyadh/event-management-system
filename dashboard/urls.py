from django.urls import path
from dashboard.views import event_dashboard, update_event, delete_event, update_category, delete_category,update_participant,delete_participant
urlpatterns = [
   path("", event_dashboard , name="dashboard"),
   path("update-event/<int:id>/", update_event, name="update-event"),
   path("delete-event/<int:id>/", delete_event, name="delete-event"),
   path("update-category/<int:id>/", update_category, name="update-category" ),
   path("delete-category/<int:id>/", delete_category, name="delete-category"),
   path("update-participant/<int:id>/", update_participant, name="update-participant"),
   path("delete-participant/<int:id>/", delete_participant, name="delete-participant")
]