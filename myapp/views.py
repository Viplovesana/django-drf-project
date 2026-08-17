from django.shortcuts import render
from myapp.models import Student
from myapp.serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

# Create your views here.
# ============================ COMBINE VIEW ==========================================================>>
'''@csrf_exempt
def combine_api(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=py_data,many=True)
        if serializer.is_valid():
            serializer.save()
            msg = {"msg":"data succesfully created"}
            json_msg = JSONRenderer().render(msg)
            return HttpResponse(json_msg,content_type = "application/json")
        else:
            msg = {"msg":"data not created"}
            json_msg = JSONRenderer().render(msg)
            return HttpResponse(json_msg,content_type = "application/json")   

    elif request.method == "GET":
        py_data = Student.objects.all()
        serializer=StudentSerializer(py_data,many=True)
        return JsonResponse(serializer.data,safe=False)   

    elif request.method == "PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        old_data = Student.objects.get(id = py_data.get('id'))
        print(old_data)
        serializer = StudentSerializer(old_data,data=py_data)
        if serializer.is_valid():
            serializer.save()
            msg = {"msg":"data updated succesfully"}
            json_msg = JSONRenderer().render(msg)
            return HttpResponse(json_msg,content_type = "application/json")
        else:
            msg = {"msg":"data not updated"}
            json_msg = JSONRenderer().render(msg)
            return HttpResponse(json_msg,content_type = "application/json") 

    elif request.method == "PATCH":
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        old_data = Student.objects.get(id = py_data.get('id'))
        serializer = StudentSerializer(old_data,data = py_data, partial = True)
        if serializer.is_valid():
            serializer.save()  
            msg = {"msg":"data partially updated succesfully"}
            json_msg = JSONRenderer().render(msg)
            return HttpResponse(json_msg,content_type = "application/json")
        else:
            msg = {"msg":"data not updated"}
            json_msg = JSONRenderer().render(msg)
            return HttpResponse(json_msg,content_type = "application/json") 

    elif request.method =="DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        stu_data = Student.objects.get(id = py_data.get('id'))
        stu_data.delete()
        msg = {"msg":"data deleted"}
        j_msg = JSONRenderer().render(msg)
        return HttpResponse(j_msg,content_type = "application/json") '''
                                 
# ============================ FUNCTION BASED VIEW DRF ===============================================>>
'''@csrf_exempt
def student_list(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=py_data,many=True)
        if serializer.is_valid():
            serializer.save()
            msg = {"msg":"data created succesfully"}
            json_msg = JSONRenderer().render(msg)       
        return HttpResponse(json_msg,content_type = "application/json")            

    py_data = Student.objects.all()
    serializer = StudentSerializer(py_data,many=True)
    return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def student_detail(request,pk):
    if request.method == "PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        old_data = Student.objects.get(id=pk)
        serializer = StudentSerializer(old_data,data=py_data)
        if serializer.is_valid():
            serializer.save()
            msg = {"msg":"data updated successfully"}
            show_msg = JSONRenderer().render(msg)
            return HttpResponse(show_msg,content_type="application/json")
        else:
            msg = {"msg":"data not updated!!"}
            show_msg = JSONRenderer().render(msg)
            return HttpResponse(show_msg,content_type="application/json")            

    elif request.method == "PATCH":
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        old_data= Student.objects.get(id=pk)
        serializer = StudentSerializer(old_data,data = py_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            msg = {"msg":"data partially updated"}
            json_msg = JSONRenderer().render(msg)
            return HttpResponse(json_msg,content_type="application/json")
        else:
            msg = {"msg":"data partially not updated"}
            json_msg = JSONRenderer().render(msg)
            return HttpResponse(json_msg,content_type="application/json")            

    elif request.method == "DELETE":
        dlt_data = Student.objects.get(id=pk)
        dlt_data.delete()
        msg = {"msg":"data deleted succesfully"}
        json_msg = JSONRenderer().render(msg)
        return HttpResponse(json_msg,content_type = "application/json")'''



# ----------------------------------------API-VIEWS---------------------------------------------------------

from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
# from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes,authentication_classes

@api_view(['GET'])
@permission_classes([IsAuthenticated])
# @authentication_classes([BasicAuthentication])
@authentication_classes([TokenAuthentication])
def protected_api(request):
    return Response({
        "msg": "You are authenticated",
        "user": request.user.username,
        "branch":"login-features"
    })