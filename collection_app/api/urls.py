from django.urls import path
from collection_app.api.views import CollectionListAV, CollectionDetailsAV
from collection_app.api.views import CollectionTransactionListAV, CollectionTransactionDetailsAV, CollectionViewSet

urlpatterns = [
    path('', CollectionListAV.as_view(), name='collection-list-info'),
    path('<int:pk>/', CollectionDetailsAV.as_view(), name='collection-details'),

    path("save_collection/", CollectionViewSet.as_view({"post": "create"})),

    path('transaction/', CollectionTransactionListAV.as_view(), name='collection-transaction-list-info'),
    path('transaction/<int:pk>/', CollectionTransactionDetailsAV.as_view(), name='collection-transaction-details'),
]