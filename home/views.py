from django.shortcuts import render, redirect
from events.forms import ParticipantModelForm
from events.models import Event
from django.contrib import messages
from django.db.models import Q

# Create your views here.

def home(request):
   participant = ParticipantModelForm()
   base_query = Event.objects.select_related('category').prefetch_related('participants').all()
   search_query = request.GET.get('search')
   if search_query:
      base_query = base_query.filter(
        Q(title__icontains=search_query) |
        Q(category__name__icontains=search_query) |
        Q(location__icontains=search_query)
    )

   if request.method=="POST":
      participant = ParticipantModelForm(request.POST)

      if participant.is_valid():
         participant.save()
         messages.success(request, "Participant created successfully")
         return redirect("home")
      else:
         messages.error(request,"There was an error in the form. Please check your inputs")


   context={
      'participant_form': participant,
      'events':base_query

   }

   return render(request, 'home.html', context)
