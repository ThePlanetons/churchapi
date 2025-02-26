from rest_framework import serializers
from collection_app.models import collection, collection_transaction

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = collection
        fields = '__all__'

class CollectionTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = collection_transaction
        fields = '__all__'