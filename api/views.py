from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from .serializers import UserCreateSerializer, CoffeeBeanListSerializer, CoffeeBeanDetailSerializer, CartItemSerializer, UserLoginSerializer
from api.models import *
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework import serializers
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer
    token = serializers.CharField(allow_blank=True, read_only=True)

    def post(self, request):
        my_data = request.data
        serializer = UserLoginSerializer(data=my_data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class CoffeeBeanListView(ListAPIView):
    queryset = CoffeeBean.objects.all()
    serializer_class = CoffeeBeanListSerializer

class CoffeeBeanDetailView(RetrieveAPIView):
    queryset = CoffeeBean.objects.all()
    serializer_class = CoffeeBeanDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'
    # permission_classes = [IsAuthenticated]


class CheckOutCoffeeBean(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request):
        order_obj = Order.objects.get(user=request.user, completed_order=False)
        order_obj.completed_order = True
        order_obj.save() 
        return Response(status= HTTP_200_OK)



class CoffeeBeanCart(CreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
      order_obj, created = Order.objects.get_or_create(user=self.request.user, completed_order=False)
      serializer.save(order=order_obj)


