from .models import CandidateApplied, Job
from rest_framework import serializers


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class CandidateAppliedSerializer(serializers.ModelSerializer):
    job = JobSerializer()

    class Meta:
        model = CandidateApplied
        fields = [
            'user',
            'resume',
            'applied_at',
            'job'
        ]
        