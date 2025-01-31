from rest_framework.response import Response
from rest_framework import status, generics, filters
from entity_app.models import *
from entity_app.api.serializers import *

# from churchapi.pagination import pagePagination

# Entity - List Create
class EntityListAV(generics.ListCreateAPIView):
    serializer_class = EntitySerializer
    # pagination_class = pagePagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['code', 'name']
    def get_queryset(self):
        entityInfo = entity.objects.filter()
        return entityInfo

# Entity - Retrieve Update Destroy
class EntityDetailsAV(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EntitySerializer
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        entityDetails = entity.objects.filter(id=pk)
        return entityDetails
    # def delete(self, request, *args, **kwargs):
    #     pk = self.kwargs.get('pk')
    #     membershipDetails = member.objects.filter(id=pk).select_related('staff_id')
    #     membershipDetails.delete()
    #     return Response(status=status.HTTP_200_OK)