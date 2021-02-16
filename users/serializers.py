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
      'confirmed_email',
      'is_admin',
    ]
  
  def get_avatar(self, obj):
    return obj.avatar.url if obj.avatar else settings.MEDIA_URL + \
        'default_avatar.png'

class UserWriteSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = [
      'first_name',
      'last_name',
      'email',
      'password',
    ]

  def create(self, validated_data):
    password = validated_data.pop('password')
    user = super().create(validated_data)
    user.set_password(password)
    user.save()
    return user
