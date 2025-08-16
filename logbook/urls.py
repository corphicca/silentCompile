from django.urls import path 
from . import views 

urlpatterns = [
    #list all entries 
    path('entries/', views.entry_list, name='entry_list'),
    #form to create a new entry
    path('entries/new/', views.create_entry, name='create_entry'), 
    #user registration page
    path('signup/', views.signup_view, name= 'signup'),
    #path('profile/', views.profile_view, name='profile'),
]