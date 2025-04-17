from django.shortcuts import render,redirect
from django.http import HttpResponse
from events.forms import EventModelForm,EventCategoryModelForm, ParticipantModelForm
from django.contrib import messages
from events.models import Category


# Dashboard
def dashboard(request):
   return render(request, 'dashboard.html')

# Create event here
def create_event(request):
    form = EventModelForm()
    category = EventCategoryModelForm()

    if request.method=="POST":
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
        
    return render(request, 'event_form.html', context)              

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

   return render(request, 'participant_form.html', context)

# Update category here
def update_category(request, id):
   updated_category = Category.objects.get(id=id)
   category = EventCategoryModelForm(instance=update_category)
   if request.method=="POST":
      category = EventCategoryModelForm(request.POST, instance=update_category)
      if category.is_valid():
         category.save()
         messages.success(request, "Updated category successfully")
      else:
         messages.error(request, "Something went wrong")
   
   context={
      'category_form':category
   }
   return render(request, 'category_form.html', context)