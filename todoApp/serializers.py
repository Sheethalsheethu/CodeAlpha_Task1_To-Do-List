from rest_framework import serializers
from todoApp.models import todo

class todoSerializer(serializers.ModelSerializer):
    class Meta:
        model = todo
        fields = '__all__'