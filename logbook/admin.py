from django.contrib import admin
from .models import Entry, Tag, Programmer, Milestone, ProgrammerMilestone, EntryTag

# Register your models here.
admin.site.register(ProgrammerMilestone) #Link Programmer and Milestone along with achieved date
admin.site.register(EntryTag) #Link Entry and Tag 
admin.site.register(Entry) #has a foreign key to Programmer 
admin.site.register(Tag)
admin.site.register(Programmer)
admin.site.register(Milestone)
