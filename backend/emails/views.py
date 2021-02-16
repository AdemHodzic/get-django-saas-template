from django.shortcuts import render

from django.http import HttpResponse
from django.utils.http import urlsafe_base64_decode

from users.models import User

from .tokens import account_activation_token

def activate(request, id, token):
  try:
    uid = urlsafe_base64_decode(id).decode()
    user = User.objects.get(pk=uid)
    
    if user is None or not account_activation_token.check_token(user, token):
      raise Exception('Invalid User')
    
    user.confirmed_email = True
    user.save()
    return HttpResponse('Hello World')
  except Exception as e:
    print(e)
    return HttpResponse('Invalid url', status=400)