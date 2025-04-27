from django.shortcuts import render,redirect
from django.http import HttpResponse
from events.forms import EventModelForm,EventCategoryModelForm, ParticipantModelForm
from django.contrib import messages
from events.models import Category


# Create event here
def create_event(request):
    form = EventModelForm()
    category = EventCategoryModelForm()

    if request.method == "POST":
        form = EventModelForm(request.POST)
        category = EventCategoryModelForm(request.POST)

        if form.is_valid() and category.is_valid():
         category_instance = category.save()
         form_instance = form.save(commit=False)
         form_instance.category = category_instance
         form_instance.save()

         messages.success(request, "Created event successfully")
         return redirect("event")
        else:
           messages.error(request, "There was an error in the form. Please check your inputs.")

    context ={
        "event_form":form,
        'category_form': category
    }
        
    return render(request, 'event.html', context)              

# Create participant here
def create_participant(request):
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

   return render(request, 'participant.html', context)

# Create category from here
def create_category(request):
   form = EventCategoryModelForm()

   if request.method=="POST":
      form = EventCategoryModelForm(request.POST)
      if form.is_valid():
         form.save()
         messages.success(request, "Created category successfully")
      else:
         messages.error(request, "Something went wrong")
   
   context={
      'category_form':form
   }
   return render(request, 'category.html', context)