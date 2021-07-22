from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import exceptions
from restapidjango.models import UserProfile
from restapidjango.readcard_functions import *
from restapidjango.readcard_class import *
import restframeworkdjango.settings as settings
import sys

# Create your views here.
class HelloApi(APIView):
    
    def get(self, request, format=None):
        username = request.META.get('HTTP_USERNAME')
        token = request.META.get('HTTP_TOKEN')
        respuesta1 = {"message":"Hola Mundo desde la API", "username":username, "token": token}
        return Response(respuesta1)

class pruebaAuth(APIView):

    def get(self,request,forma=None):
        username = request.META.get('HTTP_USERNAME')
        token = request.META.get('HTTP_TOKEN')
        try:
            uservalidation = UserProfile.objects.filter(email=username).values('id')
            dict_user = uservalidation[0]
            validate_id = dict_user['id']
            tokenvalidation = Token.objects.filter(user_id=validate_id).values('key')
            dict_token = tokenvalidation[0]
            value_token = dict_token['key']
            if token == value_token:
                validationauth = True
            else:
                validationauth = False
            respuesta1 = {"message":"Hola Mundo desde la API", "username":username, "token": token, "Validacion_Login":validationauth}
            if validationauth:
                keylogfile = readkeylog(settings.STATIC_URL+'keylog.txt')
                keylogfile.getlistnumbers()
            return Response(respuesta1)
        except Exception as e:
            return Response({"mesagge":str(e)})
        