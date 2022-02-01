from rest_framework import serializers
from .models import *


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class MeasurementSerializer(serializers.ModelSerializer):

    screen = serializers.ImageField(max_length=None,
                                    use_url=True,
                                    allow_null=True,
                                    required=False
                                    )

    class Meta:
        model = Measurement
        fields = '__all__'
