from rest_framework import routers

from users.views import UserViewSet

router = routers.DefaultRouter()
router.trailing_slash = '/?'

router.register(r'users', UserViewSet)
