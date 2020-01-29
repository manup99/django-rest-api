from rest_framework import serializers

from .models import Status
'''Serializers->JSON'''
'''Serializers->validate Data'''
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model=Status
        fields=[
            'user',
            'image',
            'content',
            'id'
        ]
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