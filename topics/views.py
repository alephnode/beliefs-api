from rest_framework import authentication, permissions, viewsets
from .models import Topic
from .serializers import TopicSerializer, TopicReadSerializer

class DefaultsMixin(object):                                           
    """Default settings for view authentication, permissions,
    filtering and pagination."""

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class TopicViewSet(viewsets.ModelViewSet):

    queryset = Topic.objects.order_by('id')
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TopicReadSerializer
        return TopicSerializer