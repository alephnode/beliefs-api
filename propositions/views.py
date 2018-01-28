from rest_framework import authentication, permissions, viewsets
from .models import Proposition
from .serializers import PropositionSerializer

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


class PropositionViewSet(viewsets.ModelViewSet):

    queryset = Proposition.objects.order_by('id')
    serializer_class = PropositionSerializer