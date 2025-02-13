from django.urls import path
from entity_app.api.views import EntityListAV, EntityDetailsAV

urlpatterns = [
    path('', EntityListAV.as_view(), name='entity-list-info'),
    path('<int:pk>/', EntityDetailsAV.as_view(), name='entity-details'),
]