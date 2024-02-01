from rest_framework import serializers


class PublisherSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=300)
