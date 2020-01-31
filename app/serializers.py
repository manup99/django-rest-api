from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Status
'''Serializers->JSON'''
'''Serializers->validate Data'''
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print('hello')
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model=Status
        fields=[
            'user',
            'image',
            'content',
            'id'
        ]
    read_only_fields=['user']
    # def valid_<field name>(self,value)
    def valid_content(self,value):
        if len(value)>10:
            raise serializers.ValidationError("Too long")
        return value
    # for all field validate
    def validate(self,data):
        content=data.get("content",None)
        if content=="":
            content=None
        image=data.get("image",None)
        if content is None and image is None:
            raise serializers.ValidationError("COntent and image cannot be null")
        return data