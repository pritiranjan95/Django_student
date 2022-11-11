from .models import Student_details
from rest_framework import serializers

class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model=Student_details
        fields="__all__"
        