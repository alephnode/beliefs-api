from rest_framework import serializers
from .models import Source
from propositions.models import Proposition
from propositions.serializers import PropositionSerializer

class SourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Source
        fields = ('id', 'created_at', 'updated_at', 'name', 'link', 'propositions')

class SourceReadSerializer(SourceSerializer):
    propositions = PropositionSerializer(many=True, read_only=True)