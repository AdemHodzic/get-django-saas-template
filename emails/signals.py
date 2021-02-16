from django.dispatch import Signal

from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

from django.core.mail import send_mail

from django.conf import settings

from django.template.loader import render_to_string

from django.contrib.sites.shortcuts import get_current_site

from .tokens import account_activation_token

def on_send_confirmation_email(sender, request, user, *args, **kwargs):
  domain = get_current_site(request).domain
  id = urlsafe_base64_encode(force_bytes(user.pk))
  token = account_activation_token.make_token(user)

  mail = render_to_string('emails/confirm_email.html', {
    'user': user,
    'domain': domain,
    'id': id,
    'token': token,
  })

  send_mail('Confirm Your Account', mail, settings.DEFAULT_EMAIL, [user.email], fail_silently=False)

SendConfirmationEmail = Signal()

SendConfirmationEmail.connect(on_send_confirmation_email)
