from rest_framework import serializers
from .models import Proposition

class PropositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proposition
        fields = ('id', 'created_at', 'updated_at', 'text', 'veracity')
