from rest_framework import serializers
from collection_app.models import collection, collection_transaction

class CollectionSerializer(serializers.ModelSerializer):
    first_approver_name = serializers.SerializerMethodField()
    second_approver_name = serializers.SerializerMethodField()
    transactions = serializers.SerializerMethodField()

    class Meta:
        model = collection
        fields = '__all__'

    def get_first_approver_name(self, obj):
        if obj.first_approver:
            return f"{obj.first_approver.first_name} {obj.first_approver.last_name}"
        return None

    def get_second_approver_name(self, obj):
        if obj.second_approver:
            return f"{obj.second_approver.first_name} {obj.second_approver.last_name}"
        return None

    def get_transactions(self, obj):
        transactions = {
            "Tithes": CollectionTransactionSerializer(obj.ct_collection_id.filter(collection_type="Tithes").select_related('member', 'collection'), many=True).data,
            "Mission": CollectionTransactionSerializer(obj.ct_collection_id.filter(collection_type="Mission").select_related('member', 'collection'), many=True).data,
            "Partnership": CollectionTransactionSerializer(obj.ct_collection_id.filter(collection_type="Partnership").select_related('member', 'collection'), many=True).data,
            "Offering": CollectionTransactionSerializer(obj.ct_collection_id.filter(collection_type="Offering").select_related('member', 'collection'), many=True).data,
            "Normal": CollectionTransactionSerializer(obj.ct_collection_id.filter(collection_type="Normal").select_related('member', 'collection'), many=True).data,
        }

        # Calculate Grand Total
        grand_total = 0
        for key in transactions:
            total = sum(float(t["collection_amount"]) for t in transactions[key] if "collection_amount" in t)
            grand_total += total

        transactions["grand_total"] = grand_total

        return transactions

class CollectionTransactionSerializer(serializers.ModelSerializer):
    member_name = serializers.SerializerMethodField()

    def get_member_name(self, obj):
        if obj.member:
            return f"{obj.member.first_name} {obj.member.last_name}"
        return None

    class Meta:
        model = collection_transaction
        fields = '__all__'