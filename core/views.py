from django.shortcuts import render
from . import models
from .serializers import UpoloaderrSerializer
# Create your views here
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser,FileUploadParser
from rest_framework import status, permissions
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

class DepartmentView(APIView):
    parser_classes = (MultiPartParser,)

    def get(self, request, *args, **kwargs):
    
        email  = request.GET.get("email")
        if email:
            snippets = models.uploader.objects.filter(email=email)
            try:
                serializer = UpoloaderrSerializer(snippets, many=True)
                lis=[]
                for i in serializer.data:
                    lis.append(i['file'])
                print(lis)
                if len(lis) == 0:
                    dicti = {
                        'status':'failed',
                        'message':'Not Found'
                    }
                    return Response(dicti)
                    
                else:
                    dicti = {
                        'status':'sucess',
                        'email': email,
                        'files':lis
                    }
                    return Response(dicti)
            except:
                dicti = {
                'status':'failed',
                }
                return Response(dicti)
                
        else:
            dicti = {
                'status':'failed',
            }
            return Response(dicti)
            
    def post(self, request, *args, **kwargs):
        department_serializer = UpoloaderrSerializer(data=request.data)
        if department_serializer.is_valid():
            department_serializer.save()
            response = Response(department_serializer.data, status=status.HTTP_201_CREATED)
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
            return response
        else:
            print(department_serializer.errors)
            return Response(department_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
