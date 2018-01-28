from rest_framework import serializers
from .models import Topic
from beliefs.models import Belief
from beliefs.serializers import BeliefSerializer

class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = ('id', 'created_at', 'updated_at', 'name', 'beliefs')

class TopicReadSerializer(TopicSerializer):
    beliefs = BeliefSerializer(many=True, read_only=True)