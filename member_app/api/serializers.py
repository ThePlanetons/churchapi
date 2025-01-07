from rest_framework import serializers
from member_app.models import member

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = member
        fields = '__all__'