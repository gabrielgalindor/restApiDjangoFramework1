from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import exceptions
from restapidjango.models import UserProfile


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
            tokenvalidation = Token.objects.filter(user_id=1).values('key')
            dict_token = tokenvalidation[0]
            value_token = dict_token['key']
            if token == value_token:
                validationauth = True
            else:
                validationauth = False
            respuesta1 = {"message":"Hola Mundo desde la API", "username":username, "token": token, "Validacion_Login":validationauth}
            return Response(respuesta1)
        except:
            return Response({"mesagge":"error ha ingresado un usuario o token no valido"})
        