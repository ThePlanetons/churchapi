from rest_framework.response import Response
from rest_framework import status, generics, filters
from collection_app.models import *
from collection_app.api.serializers import *

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from collection_app.models import collection, collection_transaction
from member_app.models import member

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

class CollectionViewSet(viewsets.ViewSet):
    @transaction.atomic
    def create(self, request):
        try:
            # Save Collection
            first_approver = member.objects.get(id=request.data["first_approver"])
            second_approver = member.objects.get(id=request.data["second_approver"])

            collection_obj = collection.objects.create(
                first_approver=first_approver,
                second_approver=second_approver
            )

            # Save Collection Transactions
            collection_types = ["Tithes", "Mission", "Partnership", "Offering"]

            for collection_type in collection_types:
                transactions = request.data.get(collection_type, [])

                for item in transactions:
                    member_id = item.get("member")
                    member_obj = member.objects.get(id=member_id) if member_id else None

                    collection_transaction.objects.create(
                        member=member_obj,
                        collection_type=collection_type,
                        collection_amount=item.get("collection_amount"),
                        transaction_date=item.get("transaction_date"),
                        transaction_type=item.get("transaction_type")
                    )

            return Response({"message": "Saved Successfully"}, status=status.HTTP_201_CREATED)

        except member.DoesNotExist:
            return Response({"message": "Member Not Found"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)