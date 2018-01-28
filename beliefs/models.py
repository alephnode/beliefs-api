from django.db import models
from propositions.models import Proposition

class Belief(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=500)
    propositions = models.ManyToManyField(Proposition, blank=True, related_name='beliefs_from_proposition')
    veracity = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.text
    
    class Meta:
        ordering = ('id',)
        db_table = 'beliefs'
