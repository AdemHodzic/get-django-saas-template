from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.utils.http import urlsafe_base64_decode

from users.models import User

from .tokens import account_activation_token

def activate(request, id, token):
  try:
    uid = urlsafe_base64_decode(id).decode()
    user = User.objects.get(pk=uid)
    
    if user is None or not account_activation_token.check_token(user, token) or user.confirmed_email:
      raise Exception('Invalid User')
    
    user.confirmed_email = True
    user.save()
    return redirect('emails:activate_success')
  except Exception as e:
    print(e)
    return redirect('emails:activate_fail')

def activate_success(request):
  return render(request, 'emails/activate_success.html')

def activate_fail(request):
  return render(request, 'emails/activate_fail.html')
