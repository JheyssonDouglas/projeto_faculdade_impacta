from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from django.contrib.auth import get_user_model, authenticate, login
from .models import Product, CartItem, CustomUser
from .serializers import ProductSerializer, UserSerializer, CartItemSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.authtoken.models import Token

User = get_user_model()

@permission_classes([AllowAny])
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    """Registra um novo usuário no sistema"""
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'success': True, 'message': 'Usuário cadastrado!'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    """Autentica um usuário"""
    email = request.data.get('email')
    password = request.data.get('password')
    
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'success': True, 'token': token.key, 'message': 'Login realizado com sucesso!'}, status=status.HTTP_200_OK)
    else:
        return Response({'success': False, 'message': 'Email ou senha incorretos.'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([AllowAny])
def user_cart(request):
    user = request.user if request.user.is_authenticated else None
    
    if request.method == 'GET':
        # Verifica se existe um carrinho ativo para o usuário
        if user:
            # Carrinho de um usuário autenticado
            cart_items = CartItem.objects.filter(user=user, is_active=True)
        else:
            # Carrinho anônimo
            cart_items = CartItem.objects.filter(user=None, is_active=True)
        
        # Caso o carrinho esteja vazio, perguntar se quer continuar ou iniciar novo
        if not cart_items.exists():
            return Response({
                'success': False,
                'message': 'Carrinho vazio. Você deseja continuar com sua compra anterior ou iniciar um novo carrinho?'
            }, status=status.HTTP_200_OK)
        
        # Se há itens no carrinho, retorna esses itens
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Limpa o carrinho anterior se o usuário optar por iniciar uma nova compra
        if 'start_new' in request.data and request.data['start_new'] == True:
            if user:
                CartItem.objects.filter(user=user, is_active=True).update(is_active=False)
            else:
                CartItem.objects.filter(user=None, is_active=True).update(is_active=False)
        
        # Adiciona os itens ao carrinho
        for item in request.data.get('items', []):
            CartItem.objects.create(
                user=user,
                product_id=item['product']['id'],
                quantity=item['quantity'],
                is_active=True
            )
        
        return Response({'success': True}, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        # Limpa o carrinho
        if user:
            CartItem.objects.filter(user=user, is_active=True).delete()
        else:
            CartItem.objects.filter(user=None, is_active=True).delete()

        return Response({'success': True}, status=status.HTTP_204_NO_CONTENT)
