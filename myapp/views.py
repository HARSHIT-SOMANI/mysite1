
from django.shortcuts import render
# Create your views here.
def index(request):
    print('inside index')
    return render(request,'index.html')


#def user(request):
#    print('########################insideticketlist1')
#    if request.method=='POST':
#        print('######cvme to sinup1')
#        name=request.POST['name']
##        email=request.POST['email']
#       phoneNumber=request.POST['phoneNumber']
#        regId=request.POST['regId']
#        address=request.POST['address']
#        k=business_registration.objects.create(name=name,email=email,phoneNumber=phoneNumber,regId=regId,address=address)
#    return render(request,'index.html')
