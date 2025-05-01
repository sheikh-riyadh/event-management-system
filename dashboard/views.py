from django.shortcuts import render, redirect
from events.models import Category, Event, Participant
from events.forms import EventCategoryModelForm, EventModelForm,ParticipantModelForm
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def event_dashboard(request):
   request_type = request.GET.get('type', 'event')
   filter_data = request.GET.get('selected_category')
   data = None

   if request_type == 'event':
      qs = Event.objects.select_related('category').prefetch_related('participants')
      if filter_data:
         qs = qs.filter(category__name=filter_data)
      data = qs

   elif request_type == 'category':
      qs = Category.objects.prefetch_related('events')
      if filter_data:
         qs = qs.filter(name=filter_data)
      data = qs

   else:
      # No filter_data needed here since participant has no direct category
      data = Participant.objects.prefetch_related('events__category')



   context={
      'data' : data,
      'request_type' : request_type,
      'url_name' : f"create-{request_type}",
      'button_name' : f"Create {request_type}",
      'categories': Category.objects.all()
   }

   return render(request, 'dashboard.html', context)

def update_event(request, id):
   update_event = Event.objects.get(id=id)
   form = EventModelForm(instance=update_event)

   if request.method == 'POST':
      form = EventModelForm(request.POST, instance=update_event)
      if form.is_valid():
         form.save()
         url = reverse('dashboard')
         return redirect(f'{url}?type=event')

   context = {
      'event_form':form
   }

   return render(request, 'event.html', context)

def delete_event(request, id):
   delete_item = Event.objects.get(id=id)

   if request.method == 'POST':
      if delete_item:
         delete_item.delete()
         url = reverse('dashboard')
         return redirect(f'{url}?type=event')

def update_category(request, id):
   updated_category = Category.objects.get(id=id)
   form = EventCategoryModelForm(instance=updated_category)

   if request.method == 'POST':
      form = EventCategoryModelForm(request.POST, instance=updated_category)
      if form.is_valid():
         form.save()
         url = reverse('dashboard')
         return redirect(f'{url}?type=category')
   
   context={
      'category_form':form
   }

   return render(request, "category.html", context)

def delete_category(request, id):
   delete_item = Category.objects.get(id=id)
   if request.method=="POST":
      if delete_item:
         delete_item.delete()
         url = reverse('dashboard')
         return redirect(f'{url}?type=category')

def update_participant(request, id):
   update_item = Participant.objects.get(id=id)
   form = ParticipantModelForm(instance=update_item)

   if request.method == 'POST':
      form = ParticipantModelForm(request.POST, instance=update_item)
      if form.is_valid():
         form.save()
         url = reverse('dashboard')
         return redirect(f'{url}?type=participant')
   
   context={
      'participant_form': form
   }

   return render(request, 'participant.html', context)

def delete_participant(request, id):
   delete_item = Participant.objects.get(id=id)
   
   if request.method == 'POST':
      if delete_item:
         delete_item.delete()
         url = reverse('dashboard')
         return redirect(f'{url}?type=participant')