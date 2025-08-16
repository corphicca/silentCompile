from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import EntryForm, SignUpForm, ProgrammerForm
from .models import Programmer, Entry 

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

def signup_view(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        programmer_form = ProgrammerForm(request.POST)
        if user_form.is_valid() and programmer_form.is_valid():
            user = user_form.save() 
            programmer = programmer_form.save(commit=False)
            programmer.user = user 
            programmer.save() 
            login(request, user)
            return redirect('profile')
    else:
        user_form = SignUpForm()
        programmer_form = ProgrammerForm() 

    return render(request, 'logbook/signup.html', {
        'user_form': user_form, 'programmer_form': programmer_form
    })