from django.urls import path
from dashboard.views import event_dashboard, update_category,delete_category
urlpatterns = [
   path("", event_dashboard , name="dashboard"),
   path("update-category/<int:id>/", update_category, name="update-category" ),
   path("delete-category/<int:id>/", delete_category, name="delete-category")
]