from django.contrib import admin
from django.urls import path, include 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    #login and logout view using Django's built in auth system 
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    #urls from the logbook application 
    path('', include('logbook.urls')), 
]
