from rest_framework import serializers
from policyholders.models import Policyholder
class PolicyholderSerializer(serializers.ModelSerializer):
    introducer_code = serializers.CharField(source='introducer.code')
    class Meta:
        model = Policyholder
        fields = ['code', 'name', 'registration_date', 'introducer_code']
    