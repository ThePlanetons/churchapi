from rest_framework.response import Response
from rest_framework import status, generics, filters
from collection_app.models import *
from collection_app.api.serializers import *

# from churchapi.pagination import pagePagination

# Collection - List Create
class CollectionListAV(generics.ListCreateAPIView):
    serializer_class = CollectionSerializer
    # pagination_class = pagePagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    # search_fields = ['first_name', 'last_name', 'person_submitting', 'email_address', 'phone']

    def get_queryset(self):
        collectionInfo = collection.objects.filter()
        return collectionInfo

# Collection - Retrieve Update Destroy
class CollectionDetailsAV(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CollectionSerializer
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        collectionDetails = collection.objects.filter(id=pk)
        return collectionDetails

    # def delete(self, request, *args, **kwargs):
    #     pk = self.kwargs.get('pk')
    #     membershipDetails = member.objects.filter(id=pk).select_related('staff_id')
    #     membershipDetails.delete()
    #     return Response(status=status.HTTP_200_OK)

# Collection - List Create
class CollectionTransactionListAV(generics.ListCreateAPIView):
    serializer_class = CollectionTransactionSerializer
    # pagination_class = pagePagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    # search_fields = ['first_name', 'last_name', 'person_submitting', 'email_address', 'phone']

    def get_queryset(self):
        membershipInfo = collection_transaction.objects.filter()
        return membershipInfo

# Collection - Retrieve Update Destroy
class CollectionTransactionDetailsAV(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CollectionTransactionSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        membershipDetails = collection_transaction.objects.filter(id=pk)
        return membershipDetails

    # def delete(self, request, *args, **kwargs):
    #     pk = self.kwargs.get('pk')
    #     membershipDetails = member.objects.filter(id=pk).select_related('staff_id')
    #     membershipDetails.delete()
    #     return Response(status=status.HTTP_200_OK)