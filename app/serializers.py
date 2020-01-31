from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Status
from django.contrib.auth.models import User
'''Serializers->JSON'''
'''Serializers->validate Data'''
class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(style={'input_type':'password'},write_only=True)
    password1=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=User
        fields=[
            'username',
            'email',
            'password',
            'password1'
        ]
    def validate_username(self,value):
        qs=User.objects.filter(username=value)
        if qs.exists():
            raise serializers.ValidationError('A user with that username already exists')
        else:
            return value

    def validate_email(self, value):
        qs = User.objects.filter(email=value)
        if qs.exists():
            raise serializers.ValidationError('A user with that email already exists')
        else:
            return value
    def validate(self,data):
        password1=data.get('password',None)
        password2=data.get('password1',None)
        if password1!=password2:
            raise serializers.ValidationError('Sorry password do not match with each other')
        else:
            return data
    def create(self,validated_data):
        print(validated_data)
        user=User(username=validated_data.get('username'),
                  email=validated_data.get('email')
                  )
        user.set_password(validated_data.get('password'))
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