from django.shortcuts import render, redirect
from .forms import EntryForm 
from .models import Programmer, Entry 

# Create your views here.
#View 1: show all entries 
def entry_list(request):
    entries = Entry.objects.all().order_by('-createdAt')
    return render(request, 'logbook/entry_list.html', {'entries': entries})

#View 2: create a new entry 
def create_entry(request): 
    if request.method == 'POST': 
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.programmerID = Programmer.objects.first() 
            entry.save() 
            return redirect('entry_list')
    else: 
        form = EntryForm() 
        
    return render(request, 'logbook/create_entry.html', {'form': form})