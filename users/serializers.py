from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = [
      'id',
      'first_name',
      'last_name',
      'email',
      'avatar',
    ]
  
  def get_avatar(self, obj):
    return obj.avatar.url if obj.avatar else settings.MEDIA_URL + \
        'default_avatar.png'