from django.urls import re_path as url
from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from .views import MatchKillsLR, MatchKillsDTR, MatchKillsILR

from api.views import EndpointViewSet
from api.views import MLAlgorithmViewSet
from api.views import MLAlgorithmStatusViewSet
from api.views import MLRequestViewSet
from api.views import ABTestViewSet
from api.views import StopABTestView

router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", EndpointViewSet, basename="endpoints")
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register(r"mlalgorithmstatuses", MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")
router.register(r"abtests", ABTestViewSet, basename="abtests")

urlpatterns = [
    url(r"^api/v1/", include(router.urls)),
    url(
        r"^api/v1/MatchKillsLR/predict$", MatchKillsLR.as_view(), name="predict"
    ),
     url(
        r"^api/v1/MatchKillsDTR/predict$", MatchKillsDTR.as_view(), name="predict"
    ),
     url(
        r"^api/v1/MatchKillsILR/predict$", MatchKillsILR.as_view(), name="predict"
    ),
    url(
        r"^api/v1/stop_ab_test/(?P<ab_test_id>.+)", StopABTestView.as_view(), name="stop_ab"
    ),
]