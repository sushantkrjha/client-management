from rest_framework import serializers
from .models import JobSheet

class JobSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSheet
        fields = '__all__'
