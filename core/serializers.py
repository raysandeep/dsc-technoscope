from .models import uploader

from rest_framework import serializers
class UpoloaderrSerializer(serializers.ModelSerializer):
    class Meta:
        model = uploader
        fields = '__all__'