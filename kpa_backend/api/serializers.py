from rest_framework import serializers
from .models import KPAForm

class KPAFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = KPAForm
        fields = '__all__'
