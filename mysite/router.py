from myapp.viewsets import business_registrationviewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register('business_register',business_registrationviewset)