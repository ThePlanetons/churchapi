# from rest_framework.response import Response
# from rest_framework import status, generics, filters
# from member_app.models import *
# from member_app.api.serializers import *

# # from registryapi.pagination import pagePagination

# # Member - List Create
# class MemberListAV(generics.ListCreateAPIView):
#     serializer_class = MemberSerializer
#     # pagination_class = pagePagination
#     filter_backends = [filters.SearchFilter, filters.OrderingFilter]
#     search_fields = ['first_name', 'last_name', 'person_submitting', 'email_address', 'phone']
#     def get_queryset(self):
#         membershipInfo = member.objects.filter()
#         return membershipInfo

# # Member - Retrieve Update Destroy
# class MemberDetailsAV(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = MemberSerializer
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#         membershipDetails = member.objects.filter(id=pk)
#         return membershipDetails
#     # def delete(self, request, *args, **kwargs):
#     #     pk = self.kwargs.get('pk')
#     #     membershipDetails = member.objects.filter(id=pk).select_related('staff_id')
#     #     membershipDetails.delete()
#     #     return Response(status=status.HTTP_200_OK)