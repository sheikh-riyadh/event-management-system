from django.urls import path
from dashboard.views import event_dashboard, update_event, delete_event, update_category, delete_category
urlpatterns = [
   path("", event_dashboard , name="dashboard"),
   path("update-category/<int:id>/", update_category, name="update-category" ),
   path("delete-category/<int:id>/", delete_category, name="delete-category"),
   path("update-event/<int:id>/", update_event, name="update-event"),
   path("delete-event/<int:id>/", delete_event, name="delete-event")
]