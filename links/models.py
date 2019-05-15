from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Link(models.Model):
    title=models.CharField(max_length=100),
    url=models.URLField(),
    submitted_by= models.ForeignKey(User),
    upvotes=models.ManyToManyField(User, related_name='votes')
    submitted_on=models.DateTimeField(auto_now_add=True,editable=False)
    

    def __str__(self):
        return 

    def __unicode__(self):
        return 
