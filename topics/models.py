from django.db import models
from beliefs.models import Belief

class Topic(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    beliefs = models.ManyToManyField(Belief, related_name='topics_for_beliefs')
    
    class Meta:
        ordering = ('id',)
        db_table = 'topics'
