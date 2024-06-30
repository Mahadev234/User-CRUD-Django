# import serializer from rest_framework

from rest_framework import serializers

# import model from models.py
from .models import User


# Create a model serializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "firstname",
            "lastname",
            "phone",
        )
