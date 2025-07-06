from django.urls import path 
from . import views 

urlpatterns = [
    path('entries/', views.entry_list, name='entry_list'),
    path('entries/new/', views.create_entry, name='create_entry'), 
]