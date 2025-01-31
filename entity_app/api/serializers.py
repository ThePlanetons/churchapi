from rest_framework import serializers
from entity_app.models import entity

class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = entity
        fields = '__all__'