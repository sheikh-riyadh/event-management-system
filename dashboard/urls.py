from django.urls import path
from dashboard.views import event_dashboard
urlpatterns = [
   path("", event_dashboard , name="dashboard")
]