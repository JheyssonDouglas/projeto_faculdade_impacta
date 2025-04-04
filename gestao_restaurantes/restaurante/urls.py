from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, register_user, login_user, UserViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('', include(router.urls)),
]