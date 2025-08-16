from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import Entry, Tag, Programmer 

#Used for creating or editing Entry objects (did not include created_at nor programmerID)
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry 
        fields = [
            'title',
            'codeSnippet',
            'reflection',
            'sourceURL',
            'rating',
            'visibility',
        ]
        widgets = {
            'reflection': forms.Textarea(attrs={'rows':4}),
            'codeSnippet': forms.Textarea(attrs={'rows': 6}),
            'sourceURL': forms.URLInput(attrs={'placeholder': 'https://github.com/...'}),
        }

#SignUp form for Django's built-in User model 
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2') 

#for a profile page, in order to add preferred languages, or bio, or profile picture 
class ProgrammerForm(forms.ModelForm):
    class Meta:
        model = Programmer 
        fields = []