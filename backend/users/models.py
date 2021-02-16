
from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra):
        user = self.model(
            email=self.normalize_email(email),
            **extra
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password, **extra):
        user = self.create_user(
            email,
            password=password,
            **extra
        )
        user.is_admin = True
        user.save(using=self.db)
        return user

class User(AbstractUser):
    username = None
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    avatar = models.ImageField(verbose_name='Avatar', blank=True)
    confirmed_email = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin
    
    @property
    def is_superuser(self):
        return self.is_admin
    