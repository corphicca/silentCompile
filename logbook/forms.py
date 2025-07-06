from django import forms 
from .models import Entry, Tag 

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