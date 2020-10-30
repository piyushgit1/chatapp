from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from mapp.models import User, Contacts


class Userserialzier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "password", "location", "mobile_number",
                  "avtar"]

    def validate_password(self, password):
        validate_password(password=password)
        return make_password(password)


class ContactSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['users', 'first_name', 'last_name', 'mobile_number', 'profile_pic']
