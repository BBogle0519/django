from rest_framework import serializers
from .models import stepCount


class StepCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = stepCount
        fields = ('step', 'record', 'distance', 'user_id_pk')
