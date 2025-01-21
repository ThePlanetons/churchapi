from rest_framework.response import Response
from rest_framework import status, generics, filters
from member_app.models import *
from member_app.api.serializers import *

# from churchapi.pagination import pagePagination

# Member - List Create
class MemberListAV(generics.ListCreateAPIView):
    serializer_class = MemberSerializer
    # pagination_class = pagePagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'person_submitting', 'email_address', 'phone']
    def get_queryset(self):
        membershipInfo = member.objects.filter()
        return membershipInfo

# Member - Retrieve Update Destroy
class MemberDetailsAV(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MemberSerializer
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        membershipDetails = member.objects.filter(id=pk)
        return membershipDetails
    # def delete(self, request, *args, **kwargs):
    #     pk = self.kwargs.get('pk')
    #     membershipDetails = member.objects.filter(id=pk).select_related('staff_id')
    #     membershipDetails.delete()
    #     return Response(status=status.HTTP_200_OK)

class MemberConfigListAV(generics.ListCreateAPIView):
    serializer_class = MemberConfigSerializer
    # pagination_class = pagePagination
    # filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    # search_fields = ['first_name', 'last_name', 'person_submitting', 'email_address', 'phone']
    def get_queryset(self):
        membershipConfigInfo = member_config.objects.filter()
        return membershipConfigInfo

    def create(self, request, *args, **kwargs):
        # Handle list payloads
        data = request.data.get("data", None)

        if data is None:
            return Response({"error": "No data provided"}, status=status.HTTP_400_BAD_REQUEST)

        if not isinstance(data, list):
            return Response({"error": "Data must be a list"}, status=status.HTTP_400_BAD_REQUEST)

        # Validate each item in the list
        serializer = self.get_serializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)

        # Save all valid entries
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()