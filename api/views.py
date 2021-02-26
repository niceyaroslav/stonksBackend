from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView


class RegistrationApiView(APIView):

    def post(self, req):
        User.objects.create_user(req.POST['username'],
                                 req.POST['email'],
                                 req.POST['password'])
        return Response('Registration successful!')


