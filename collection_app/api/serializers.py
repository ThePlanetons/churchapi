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
        # transactions = {
        #     "Tithes": obj.ct_collection_id.filter(collection_type="Tithes").values(),
        #     "Mission": obj.ct_collection_id.filter(collection_type="Mission").values(),
        #     "Partnership": obj.ct_collection_id.filter(collection_type="Partnership").values(),
        #     "Offering": obj.ct_collection_id.filter(collection_type="Offering").values(),
        # }

        transactions = {
            "Tithes": CollectionTransactionSerializer(obj.ct_collection_id.select_related('member', 'collection').filter(collection_type="Tithes"), many=True).data,
            "Mission": CollectionTransactionSerializer(obj.ct_collection_id.select_related('member', 'collection').filter(collection_type="Mission"), many=True).data,
            "Partnership": CollectionTransactionSerializer(obj.ct_collection_id.select_related('member', 'collection').filter(collection_type="Partnership"), many=True).data,
            "Offering": CollectionTransactionSerializer(obj.ct_collection_id.select_related('member', 'collection').filter(collection_type="Offering"), many=True).data,
        }

        # Calculate Grand Total
        grand_total = 0
        for key in transactions:
            total = sum(float(t["collection_amount"]) for t in transactions[key] if "collection_amount" in t)
            grand_total += total

        transactions["grand_total"] = grand_total

        return transactions

    # def get_transactions(self, obj):
    #     collection_types = ["Tithes", "Mission", "Partnership", "Offering"]
    #     grouped = {}
    #     for type in collection_types:
    #         transactions = obj.ct_collection_id.filter(collection_type=type)
    #         grouped[type] = CollectionTransactionSerializer(transactions, many=True).data
    #     return grouped

class CollectionTransactionSerializer(serializers.ModelSerializer):
    member_name = serializers.SerializerMethodField()

    def get_member_name(self, obj):
        if obj.member:
            return f"{obj.member.first_name} {obj.member.last_name}"
        return None

    class Meta:
        model = collection_transaction
        fields = '__all__'