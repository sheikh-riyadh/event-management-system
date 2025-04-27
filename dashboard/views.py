from django.shortcuts import render, redirect
from events.models import Category, Event, Participant
from events.forms import EventCategoryModelForm
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def event_dashboard(request):
   request_type = request.GET.get('type','event')
   data= None

   if request_type == "event":
      data = Event.objects.select_related('category').prefetch_related('participants').all()
   elif request_type == "categories":
      data = Category.objects.all()
   else:
      data = Participant.objects.prefetch_related('events').all()

   context={
      'data':data,
      'type':request_type
   }

   return render(request, 'dashboard.html', context)

def update_category(request, id):
   updated_category = Category.objects.get(id=id)
   form = EventCategoryModelForm(instance=updated_category)

   if request.method == 'POST':
      form = EventCategoryModelForm(request.POST, instance=updated_category)
      if form.is_valid():
         form.save()
         url = reverse('dashboard')
         return redirect(f'{url}?type=categories')
   
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
         return redirect(f'{url}?type=categories')
      
   

