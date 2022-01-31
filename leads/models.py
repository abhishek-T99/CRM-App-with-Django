from django.db import models
from django.db import models

class Lead(models.Model):
    
    '''SOURCE_CHOICES = (
        ('YouTube', 'YouTube'),
        ('Google', 'Google'),
        ('NewsLetter', 'NewsLetter'),
    )'''
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)

    # creates leads with it's own agents hence this field is used here
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE) 
    # or models.SET_NULL(if null=true) or models.SET_DEFAULT(if default value is given)

    # phoned = models.BooleanField(default=False)
    # source = models.CharField(choices=SOURCE_CHOICES, max_length=100)

    # profile_picture = models.ImageField(blank=True, null=True)
    # special_files = models.FileField(blank=True, null=True)


'''class Agent(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)'''

