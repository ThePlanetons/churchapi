from rest_framework import serializers
from member_app.models import member, member_config

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = member
        fields = '__all__'

class MemberConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = member_config
        fields = '__all__'