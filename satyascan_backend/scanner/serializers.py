from rest_framework import serializers
from .models import ProfileScan

class ProfileScanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileScan
        fields = '__all__'