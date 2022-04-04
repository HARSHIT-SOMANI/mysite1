from rest_framework import serializers
from .models import business_registration

class business_registrationserializer(serializers.ModelSerializer):
    class Meta:
        model=business_registration
        fields='__all__'