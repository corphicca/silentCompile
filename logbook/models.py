from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Tag(models.Model):
    #tagID = models.AutoField(primary_key=True) Django auto-increment this ->only define when you want to customize it
    name = models.CharField(max_length=50, unique=True) 

    def __str__(self):
        return self.name
    
class Milestone(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name 

class Programmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username 

class Entry(models.Model):
    programmerID = models.ForeignKey("Programmer", on_delete=models.CASCADE, related_name="entries") #Foreign Key 
    title = models.CharField(max_length=50, unique=True)
    createdAt = models.DateTimeField(auto_now_add=True) 
    codeSnippet = models.TextField() 
    visibility = models.BooleanField() 
    reflection = models.TextField() 
    sourceURL = models.CharField(max_length=200)

    ratingChoices = (
        (1, "1 Star"), 
        (2, "2 Stars"),
        (3, "3 Stars"), 
        (4, "4 Stars"), 
        (5, "5 Stars"), 
    )
    rating = models.IntegerField(choices= ratingChoices,default=0)

    def __str__(self):
        return self.title
    
class ProgrammerMilestone(models.Model):
    achievedAt = models.DateTimeField(auto_now_add=True)
    programmer = models.ForeignKey("Programmer", on_delete=models.CASCADE, related_name="milestones")
    milestone = models.ForeignKey("Milestone", on_delete=models.CASCADE, related_name="ahcievements")

    def __str__(self):
        return f"{self.programmer.userName} - {self.milestone.name}"
    
class EntryTag(models.Model):
    tag = models.ForeignKey("Tag", on_delete=models.CASCADE, related_name="entry_tags")
    entry = models.ForeignKey("Entry", on_delete=models.CASCADE, related_name="entry_tags")

    def __str__(self):
        return f"{self.entry.title} tagged with {self.tag.name}"