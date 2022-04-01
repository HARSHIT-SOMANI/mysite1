from audioop import add
from .models import business_registration
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import business_registrationserializer
import json
from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect, render
# Create your views here.
def index(request):
    print('inside index')
    k=business_registration.objects.create(name='harshit')
    k.email='harshit@fininfo.com'
    k.phoneNumber='9849549307'
    k.address='d.no-17/92'
    k.regId='123'
    k.save()
    return render(request,'index.html')


def user(request):
    print('########################insideticketlist1')
    if request.method=='POST':
        print('######cvme to sinup1')
        name=request.POST['name']
        email=request.POST['email']
        phoneNumber=request.POST['phoneNumber']
        regId=request.POST['regId']
        address=request.POST['address']
        k=business_registration.objects.create(name=name,email=email,phoneNumber=phoneNumber,regId=regId,address=address)
    return render(request,'index.html')
