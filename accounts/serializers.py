from rest_framework import serializers
# from .models import User
# instead of directly importing User model, import the model defined in AUTH_USER_MODEL
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) # write_only=True ensures this data won't be sent in the response to frontend
    password2 = serializers.CharField(write_only=True) # for confirming password 

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'bio']

    def validate(self, data):
        # data is a dictionary of all related fields
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data
        
    def create(self, validated_data):
        validated_data.pop('password2')  # remove password2 since it's not an actual db field
        return User.objects.create_user(**validated_data)
        
        #User.objects.create_user(**validated_data) is eq. to 
        # User.objects.create_user(
        #     username='john',
        #     email='john@email.com',
        #     password='abc123',
        #     bio='Hello'
        # )


