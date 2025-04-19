from django.shortcuts import render
from events.models import Category, Event, Participant

# Create your views here.
def event_dashboard(request):
   request_type = request.GET.get('type','event')
   data = None
   

   context={

   }

   return render(request, 'dashboard.html')