
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from myapp.models import business_registration
from myapp.serializers import business_registrationserializer
# Create your views here.
def index(request):
    print('inside index')
    return render(request,'index.html')


#def user(request):
#    print('########################insideticketlist1')
#    if request.method=='POST':
#        print('######cvme to sinup1')
#        name=request.POST['name']
#        email=request.POST['email']
#       phoneNumber=request.POST['phoneNumber']
#        regId=request.POST['regId']
#        address=request.POST['address']
#        k=business_registration.objects.create(name=name,email=email,phoneNumber=phoneNumber,regId=regId,address=address)
#    return render(request,'index.html')

@csrf_exempt                                                    #not required for  GET request
def user(request):
    print('########################insideticketlist1')
    print('#########################request is',request)
    if request.method=='GET':
        print('########################inside GET request')
        #articleobjects=article.objects.Get()
        #articleserilized=articleserializer(articleobjects)  if one object many=true is not needed
        businesobjects=business_registration.objects.all()
        print('##################ticketobjects is',businesobjects)
        businessserilized=business_registrationserializer(businesobjects,many=True)
        print('#####################ticketserilized is',businessserilized)
        return JsonResponse(businessserilized.data,safe=False)
    elif request.method=='POST':
        print('########################inside POST request')
        data=JSONParser().parse(request)
        print('##############data is',data)
        businessserilized=business_registrationserializer(data=data)
        print('#####################ticketserilized',businessserilized)
        if businessserilized.is_valid():
            print('########################insideticketlist4')
            businessserilized.save()
            return JsonResponse(businessserilized.data,status=201)
        return JsonResponse(businessserilized.errors,status=400)