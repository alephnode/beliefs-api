from django.db import models
from propositions.models import Proposition

class Source(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100, default='no source')
    propositions = models.ManyToManyField(Proposition, related_name='sources_for_propositions')
    
    class Meta:
        ordering = ('id',)
        db_table = 'sources'
