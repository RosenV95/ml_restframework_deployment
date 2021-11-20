from rest_framework import serializers
from apps.endpoints.models import Endpoint
from apps.endpoints.models import MLAlgorithm
from apps.endpoints.models import MLAlgorithmStatus
from apps.endpoints.models import MLReq
from django.db import models
from apps.endpoints.models import ABTest

'''
Serializers help with packing and unpacking database objects into JSON objects\
'''


class EndpointSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Endpoint
        read_only_fields = ("name", "owner", "created_at")
        fields = ("id", "name", "owner", "created_at")


class MLAlgorithmSerealizer(serializers.ModelSerializer):
    current_status = serializers.SerializerMethodField(read_only=True)
    id = serializers.ReadOnlyField()

    def get_current_status(self, mlalgorithm):
        return MLAlgorithmStatus.objects.filter(parent_mlalgorithm=mlalgorithm).latest('created_at').status

    class Meta:
        model = MLAlgorithm
        read_only_fields = ("name", "owner", "created_at", "description", "code", "version",
                            "current_status")
        fields = ("id", "name", "owner", "created_at", "description", "code", "version", "parent_endpoint",
                  "current_status")


class MLAlgorithmStatusSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = MLAlgorithmStatus
        read_only_fields = ("active")
        fields = ("id", "active", "status", "created_by", "created_at", "parent_mlalgorithm")


class MLReqSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = MLReq
        read_only_fields = (
            "input_data",
            "full_response",
            "response",
            "created_at",
            "parent_mlalgorithm",)
        fields = ("id", "input_data", "full_response", "response", "feedback", "created_at", "parent_mlalgorithm")


class ABTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ABTest
        read_only_fields = (
            "id",
            "ended_at",
            "created_at",
            "summary"
        )
        fields = (
            "id",
            "title",
            "created_by",
            "created_at",
            "ended_at",
            "summary",
            "parent_mlalgorithm_1",
            "parent_mlalgorithm_2",
        )
