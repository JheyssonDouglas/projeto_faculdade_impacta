from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, register_user, login_user, UserViewSet
from .views import user_cart, CartItemViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'users', UserViewSet)
router.register(r'cart', CartItemViewSet, basename='cart')

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('cart/', user_cart, name='user-cart'),
    path('', include(router.urls)),
]