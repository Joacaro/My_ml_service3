
from django.urls import path
from .views import MatchKillsLR, MatchKillsDTR, MatchKillsILR

urlpatterns = [
    path('MatchKillsLR/', MatchKillsLR.as_view(), name = 'MatchKillsLR'),
    path('MatchKillsDTR/', MatchKillsDTR.as_view(), name = 'MatchKillsDTR'),
    path('MatchKillsILR/', MatchKillsILR.as_view(), name = 'MatchKillsILR'),
]