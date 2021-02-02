from rest_framework import status,viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token

from django.contrib import auth

from .serializers import UserSerializer
from .models import User

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  @action(detail=False, methods=['post'], permission_classes=[AllowAny], authentication_classes=[])
  def login(self, request):
    email = request.data.get('email', None)
    password = request.data.get('password', None)
    user = auth.authenticate(username=email, password=password)

    if user and user.is_active:
      auth.login(request, user)
      serializer = UserSerializer(request.user)
      token, _ = Token.objects.get_or_create(user=user)
      return Response(data={**serializer.data,
                      'token': token.key},
                      status=status.HTTP_200_OK)
    return Response(status=status.HTTP_401_UNAUTHORIZED)
