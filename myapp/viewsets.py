from rest_framework import viewsets
from . import models
from . import serializers

class business_registrationviewset(viewsets.ModelViewSet):
    queryset=models.business_registration.objects.all()
    serializer_class=serializers.business_registrationserializer