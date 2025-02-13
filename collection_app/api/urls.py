from django.urls import path
from collection_app.api.views import CollectionListAV, CollectionDetailsAV

urlpatterns = [
    path('', CollectionListAV.as_view(), name='collection-list-info'),
    path('<int:pk>/', CollectionDetailsAV.as_view(), name='collection-details'),
]