from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet, EmployeeViewSet, DishViewSet, OrderViewSet, StockViewSet, ReservationViewSet

router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'dishes', DishViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'stocks', StockViewSet)
router.register(r'reservations', ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]