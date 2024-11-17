from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name', 'mobile_number', 'city', 'referral_code', 'password', 'referrer']
        extra_kwargs = {'password': {'write_only': True}}  # Hide passwords in responses
