from rest_framework import routers
from django.conf.urls import include, url

from beliefs.views import BeliefViewSet
from propositions.views import PropositionViewSet
from sources.views import SourceViewSet
from topics.views import TopicViewSet

router = routers.DefaultRouter()
router.register(r'beliefs', BeliefViewSet, base_name='belief')
router.register(r'propositions', PropositionViewSet, base_name='proposition')
router.register(r'sources', SourceViewSet, base_name='source')
router.register(r'topics', TopicViewSet, base_name='topic')

urlpatterns = [
    url(r'^api/',include(router.urls)),
    url(r'^api-admin/', include('rest_framework.urls', namespace='rest_framework'))
]