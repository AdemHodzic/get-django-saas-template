from rest_framework import status,viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

from django.contrib import auth

from .serializers import UserSerializer, UserWriteSerializer
from .models import User

from emails.signals import SendConfirmationEmail

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
    return Response(data={"errors": ['Invalid creditentials']}, status=status.HTTP_401_UNAUTHORIZED)
    
  @action(detail=False, methods=['post'], permission_classes=[AllowAny], authentication_classes=[])
  def register(self, request):
    email = request.data.get('email', None)

    if User.objects.filter(email__iexact=email).exists():
        return Response(data={'errors': ['User already exists']}, status=400)

    serializer = UserWriteSerializer(data=request.data)

    if not serializer.is_valid():
      return Response(data=serializer.errors, status=500)

    serializer.save()

    user = User.objects.get(**serializer.data)

    SendConfirmationEmail.send(sender=self.__class__, request=request, user=user)

    token, _ = Token.objects.get_or_create(user=user)

    return Response(
        data={**UserSerializer(user).data, 'token': token.key},
        status=status.HTTP_201_CREATED)

  @action(
    detail=False, 
    methods=['post'],
    permission_classes=[AllowAny],
    authentication_classes=[TokenAuthentication])
  def logout(self, request):
      auth.logout(request)
      return Response(status=status.HTTP_200_OK)

  @action(detail=False, methods=['GET'], permission_classes=[AllowAny], authentication_classes=[TokenAuthentication])
  def profile(self, request):
    if request.auth is not None :
      serializer = UserSerializer(request.user)
      token, _ = Token.objects.get_or_create(user=request.user)
      return Response(status=status.HTTP_200_OK,
                      data={**serializer.data,
                            'token': token.key,})
    return Response(status=status.HTTP_401_UNAUTHORIZED)