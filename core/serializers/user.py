from core.models.user import User
from rest_framework import serializers





class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'uid']

