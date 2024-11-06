from rest_framework.serializers import Serializer, ModelSerializer
from .models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersModel
        fields = "__all__"