from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from mapp.models import User, Contacts
from mapp.serializer import Userserialzier, ContactSerialzier
from mapp.verifier import a

account_sid = "AC385ec85d7daad07ea99e4852e248ab7a"
auth_token = "7f2ff290155ceae84c722ce8e56a6a29"

import requests

url = "https://www.fast2sms.com/dev/bulk"


class user(APIView):

    def get(self, request):
        user = User.objects.all()
        serializer = Userserialzier(user, many=True)
        return Response(serializer.data, status=201)

    def post(self, request):
        serialilzer = Userserialzier(data=request.data)
        if serialilzer.is_valid(raise_exception=True):
            serialilzer.save()
        return Response(serialilzer.data)

    def delete(self, request):
        user_obj = User.objects.all()
        user_obj.delete()
        return Response("Objects deleted successfully")


class Putter(APIView):

    def put(self, request, pk):
        user_obj = User.objects.get(pk=pk)  
        serializer = Userserialzier(user_obj, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=201)

    def delete(self, request, pk):
        user_obj = User.objects.get(pk=pk)
        username = user_obj.username
        user_obj.delete()
        return Response('{} deleted'.format(username))


class token_generator(APIView):

    def post(self, request):
        data = JSONParser().parse(request)
        task = a.totp_obj(self)
        querystring = {
            "authorization": 'vWcAEwr3e4Q067dyTHjF5hCKStqmpfiMUI2X8Bg9uJYnzDLxVaZDtj03NWhQPVOrU5A7Kx4J6HgkXeyi',
            "sender_id": "FSTSMS", "message": "One Time Password is {}".format(task.token()),
            "language": "english", "route": "p", "numbers": data['number']}

        headers = {
            'cache-control': "no-cache"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)

        return Response(task.token())


class token_verifier(APIView):

    def post(self, request, pk):
        data = JSONParser().parse(request)

        result = a.verify_token(self, data['otp'])
        if result == True:
            data1 = {'is_verified': 'True'}
            user_obj = User.objects.get(pk=pk)
            serializer = Userserialzier(user_obj, data=data1, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(result)


class Contactview(APIView):

    def get(self, request, pk):
        user_obj = User.objects.filter(pk=pk)
        serializer = ContactSerialzier(user_obj, many=True)
        return Response(serializer.data, status=201)

    def post(self, request, pk):
        data = JSONParser().parse(request)
        data['users'] = pk
        serializer = ContactSerialzier(data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=201)

    def put(self, request, pk):
        data = JSONParser().parse(request)
        contact_obj = Contacts.objects.get(pk=pk)
        serializer = ContactSerialzier(contact_obj, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=201)

    def delete(self, request, pk):
        user_obj = Contacts.objects.get(pk=pk)
        username = user_obj.first_name
        user_obj.delete()
        return Response(username)


class site(APIView):
    def get(self, request):
        return render(request, 'mapp/index.html')


class Chatting(APIView):

    def get(self, request, room_name, user_name):
        context = {'room_name': room_name, 'user_name': user_name}
        return render(request, 'mapp/room.html', {
            "context": context})
