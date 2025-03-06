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
        collection_types = ["Tithes", "Mission", "Partnership", "Offering"]
        grouped = {}
        for type in collection_types:
            transactions = obj.ct_collection_id.filter(collection_type=type)
            grouped[type] = CollectionTransactionSerializer(transactions, many=True).data
        return grouped

class CollectionTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = collection_transaction
        fields = '__all__'