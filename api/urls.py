from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('CoffeeBeanList/', CoffeeBeanListView.as_view(), name='list'),
    path('CoffeeBeanDetail/<int:object_id>/', CoffeeBeanDetailView.as_view(), name='detail'),
    path('CoffeeBeanCart/', CoffeeBeanCart.as_view(), name='cart'),
    path('CheckOut/',CheckOutCoffeeBean.as_view(), name='check-Out'),
    path('HistoricOrder/',OrderHistoricalList.as_view(), name='historic-order')
]

