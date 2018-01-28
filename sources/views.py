from rest_framework import authentication, permissions, viewsets
from .models import Source
from .serializers import SourceSerializer, SourceReadSerializer

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


class SourceViewSet(viewsets.ModelViewSet):

    queryset = Source.objects.order_by('id')
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SourceReadSerializer
        return SourceSerializer