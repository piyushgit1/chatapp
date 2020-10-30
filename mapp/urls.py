from django import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from mapp.views import user, token_generator, token_verifier, Contactview, site, Chatting, Putter

urlpatterns = [
    path("user/", user.as_view()),
    path("token_generator/", token_generator.as_view()),
    path("token_verifier/", token_verifier.as_view()),
    path("Contact/<int:pk>/", Contactview.as_view()),
    path('finder/<int:pk>/', Putter.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('site/', site.as_view()),
    path('<str:user_name>/<str:room_name>/', Chatting.as_view()),

]
