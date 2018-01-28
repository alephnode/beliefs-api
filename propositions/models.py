from django.db import models

class Proposition(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=500)
    veracity = models.BooleanField(default=False)

    def __str__(self):
        return self.text
    
    class Meta:
        ordering = ('id',)
        db_table = 'propositions'
