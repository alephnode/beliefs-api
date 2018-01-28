from rest_framework import serializers
from .models import Belief
from propositions.models import Proposition
from propositions.serializers import PropositionSerializer

class BeliefSerializer(serializers.ModelSerializer):

    class Meta:
        model = Belief
        fields = ('id', 'created_at', 'updated_at', 'text', 'propositions', 'veracity')

class BeliefReadSerializer(BeliefSerializer):
    propositions = PropositionSerializer(many=True, read_only=True)
