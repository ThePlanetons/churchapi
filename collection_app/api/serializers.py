from rest_framework import serializers
from collection_app.models import collection

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = collection
        fields = '__all__'