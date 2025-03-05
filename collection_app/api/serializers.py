from rest_framework import serializers
from collection_app.models import collection, collection_transaction

class CollectionSerializer(serializers.ModelSerializer):
    first_approver_name = serializers.SerializerMethodField()
    second_approver_name = serializers.SerializerMethodField()

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

class CollectionTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = collection_transaction
        fields = '__all__'