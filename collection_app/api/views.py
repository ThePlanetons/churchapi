from rest_framework.response import Response
from rest_framework import status, generics, filters
from churchapi.pagination import StandardResultsSetPagination
from collection_app.models import *
from collection_app.api.serializers import *

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from collection_app.models import collection, collection_transaction
from member_app.models import member

import shortuuid

# Collection - List Create
class CollectionListAV(generics.ListCreateAPIView):
    queryset = collection.objects.select_related('first_approver', 'second_approver').all()
    pagination_class = StandardResultsSetPagination
    serializer_class = CollectionSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    # search_fields = ['first_name', 'last_name', 'person_submitting', 'email_address', 'phone']

    # def get_queryset(self):
    #     collectionInfo = collection.objects.filter()
    #     return collectionInfo

# Collection - Retrieve Update Destroy
class CollectionDetailsAV(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CollectionSerializer
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        collectionDetails = collection.objects.select_related('first_approver', 'second_approver').filter(id=pk)
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
        membershipInfo = collection_transaction.objects.select_related('member', 'collection').filter()
        return membershipInfo

# Collection - Retrieve Update Destroy
class CollectionTransactionDetailsAV(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CollectionTransactionSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        membershipDetails = collection_transaction.objects.select_related('member', 'collection').filter(id=pk)
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
            date = request.data["date"]

            collection_obj = collection.objects.create(
                first_approver=first_approver,
                second_approver=second_approver,
                date=date
            )

            # Save Collection Transactions with bulk_create
            collection_types = ["Tithes", "Mission", "Partnership", "Offering", "Normal"]
            transactions_to_create = []

            for collection_type in collection_types:
                transactions = request.data.get(collection_type, [])

                for item in transactions:
                    member_id = item.get("member")
                    member_obj = member.objects.filter(id=member_id).first() if member_id else None

                    if item.get("collection_amount"):
                        transactions_to_create.append(
                            collection_transaction(
                                collection=collection_obj,
                                member=member_obj,
                                collection_type=collection_type,
                                collection_amount=item.get("collection_amount"),
                                transaction_id=shortuuid.uuid(),
                                transaction_date=item.get("transaction_date"),
                                transaction_type=item.get("transaction_type")
                            )
                        )

            if transactions_to_create:
                collection_transaction.objects.bulk_create(transactions_to_create)

            return Response({"message": "Saved Successfully"}, status=status.HTTP_201_CREATED)

        except member.DoesNotExist:
            return Response({"message": "Member Not Found"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @transaction.atomic
    def update(self, request, pk=None):
        try:
            collection_obj = collection.objects.get(id=pk)

            # Update collection fields
            collection_obj.first_approver = member.objects.get(id=request.data["first_approver"])
            collection_obj.second_approver = member.objects.get(id=request.data["second_approver"])
            collection_obj.date = request.data["date"]
            collection_obj.save()

            collection_types = ["Tithes", "Mission", "Partnership", "Offering", "Normal"]
            existing_transactions = collection_transaction.objects.filter(collection=collection_obj)
            existing_transaction_ids = {tx.transaction_id for tx in existing_transactions}
            new_transaction_ids = set()

            for collection_type in collection_types:
                transactions = request.data.get(collection_type, [])

                for item in transactions:
                    transaction_id = item.get("transaction_id", shortuuid.uuid())  # Keep or generate new ID
                    new_transaction_ids.add(transaction_id)

                    # Check if transaction already exists
                    transaction_obj = collection_transaction.objects.filter(transaction_id=transaction_id).first()

                    if transaction_obj:
                        # Update existing transaction
                        transaction_obj.member = member.objects.filter(id=item.get("member")).first()
                        transaction_obj.collection_amount = item.get("collection_amount")
                        transaction_obj.transaction_date = item.get("transaction_date")
                        transaction_obj.transaction_type = item.get("transaction_type")
                        transaction_obj.save()
                    else:
                        # Create new transaction
                        collection_transaction.objects.create(
                            collection=collection_obj,
                            member=member.objects.filter(id=item.get("member")).first(),
                            collection_type=collection_type,
                            collection_amount=item.get("collection_amount"),
                            transaction_id=transaction_id,
                            transaction_date=item.get("transaction_date"),
                            transaction_type=item.get("transaction_type")
                        )

            # Delete transactions that were not included in the update request
            transactions_to_delete = existing_transaction_ids - new_transaction_ids
            collection_transaction.objects.filter(transaction_id__in=transactions_to_delete).delete()

            return Response({"message": "Updated Successfully"}, status=status.HTTP_200_OK)

        except collection.DoesNotExist:
            return Response({"message": "Collection Not Found"}, status=status.HTTP_404_NOT_FOUND)

        except member.DoesNotExist:
            return Response({"message": "Member Not Found"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)