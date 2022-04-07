from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from mysite.dbconn import connection
from myapp.models import business_registration

def index(request):
    return render(request,'index.html')

@csrf_exempt
def createUser(request):
    cursor = connection.cursor(prepared=True)
    data=JSONParser().parse(request)
    name=data['name']
    email=data['email']
    phoneNumber=data['phoneNumber']
    address=data['address']
    try:
       sql_lastentry_Query = "SELECT regId FROM business_registration ORDER BY regId DESC LIMIT 1"
       cursor.execute(sql_lastentry_Query)
       i = cursor.fetchone()
       i=i[0]
    except:
       i='REG10000'
    i=int(i[3:])+1
    regId='REG'+str(i)
    sql_insert_query = """ INSERT INTO business_registration (name, email, address, phoneNumber,regId) VALUES (%s,%s,%s,%s,%s)"""
    tuple1=(name,email,address,phoneNumber,regId,)
    cursor.execute(sql_insert_query, tuple1)
    connection.commit()
    data={'data':{'message' : 'user created successfully','regId':regId}}
    return JsonResponse(data,status=201)

@csrf_exempt
def updateUser(request,input):
    cursor = connection.cursor(prepared=True)
    data=JSONParser().parse(request)
    name=data['name']
    email=data['email']
    phoneNumber=data['phoneNumber']
    address=data['address']
    try:
        sql_update_query = """ UPDATE business_registration set
                       name =%s, email=%s, phoneNumber=%s, address=%s WHERE regId=%s"""
        tuple2=(name,email,phoneNumber,address,input)
        cursor.execute(sql_update_query, tuple2)
        connection.commit()
        data={'data':{'message':'user updated successfully'}}
        return JsonResponse(data,status=200,safe=False)
    except:
        JsonResponse({'message:redId not found'},status=400)

@csrf_exempt
def deleteUser(request,input):
    cursor = connection.cursor(prepared=True)
    try:
        sql_Delete_query = """Delete from  business_registration where regId = %s"""
        tuple2=(input,)
        cursor.execute(sql_Delete_query,tuple2)
        connection.commit()
        return JsonResponse({'data':{'message':'user deleted successfully'}},status=204)
    except:
        return JsonResponse({'data':{'message':'user not found'}},status=400)


@csrf_exempt
def getUser(request):
    cursor = connection.cursor(prepared=True)
    if 'regId' in request.GET:
        sql_select_Query ="""select * from business_registration WHERE regId = %s"""
        tuple2=(request.GET['regId'],)
        cursor.execute(sql_select_Query,tuple2)
        records = cursor.fetchone()
    else:
        sql_select_Query = "select * from business_registration"
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
    if(records):
        return JsonResponse(records,safe=False)
    else:
        return JsonResponse({'message':'No record found in database'},status=404)



