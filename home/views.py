from django.shortcuts import render
from events.forms import ParticipantModelForm
from django.contrib import messages

# Create your views here.

def home(request):
   participant = ParticipantModelForm()

   if request.method=="POST":
      participant = ParticipantModelForm(request.POST)

      if participant.is_valid():
         participant.save()
         messages.success(request, "Participant created successfully")
      else:
         messages.error(request,"There was an error in the form. Please check your inputs")


   context={
      'participant_form': participant
   }

   return render(request, 'home.html', context)
