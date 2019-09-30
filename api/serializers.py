from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import *
from rest_framework_jwt.settings import api_settings

class CoffeeBeanDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeBean
        fields = '__all__'

class CoffeeBeanListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeBean
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['Quant','cofeeBean']

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        
        # if (email = "");
        # email = validated_data['email']
        # new_user = User(username=username, email = email)
        
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        return validated_data

# 2

class HistoricOrderSerializer(serializers.ModelSerializer):
    # order_items = CartItemSerializer()
    order_items = serializers.SerializerMethodField()

    class Meta:
         model = Order
         fields = ['id','totalPrice','completed_order', 'order_items']

    def get_order_items(self, obj):
        order_itemsX = OrderItem.objects.filter(order=obj)
        return CartItemSerializer(order_itemsX, many=True).data 










# class UserLoginSerializer(serializers.Serializer):
#     token = serializers.CharField(allow_blank=True, read_only=True)

#     def validate(self, data):
        
#         jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
#         jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

#         payload = jwt_payload_handler(user_obj)
#         token = jwt_encode_handler(payload)

#         data["token"] = token
#         return data

# class UserLoginSerializer(serializers.Serializer):

#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)

#     def validate(self, data):
#         my_username = data.get('username')
#         my_password = data.get('password')

#         try:
#             user_obj = User.objects.get(username=my_username)
#         except:
#             raise serializers.ValidationError("This username does not exist")

#         if not user_obj.check_password(my_password):
#             raise serializers.ValidationError("Incorrect username/password combination! Try again")

#         return data

        
