from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from django.contrib.auth import get_user_model, authenticate, login
from .models import Product, CartItem, CustomUser
from .serializers import ProductSerializer, UserSerializer, CartItemSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.authtoken.models import Token

User = get_user_model()

class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

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
            cart_items = CartItem.objects.filter(user=user, is_active=True)
        else:
            cart_items = CartItem.objects.filter(user=None, is_active=True)
        
        if not cart_items.exists():
            return Response({
                'success': False,
                'message': 'Carrinho vazio. Você deseja continuar com sua compra anterior ou iniciar um novo carrinho?'
            }, status=status.HTTP_200_OK)
        
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
    # Log para verificar os dados recebidos
        print(f"Dados recebidos no POST: {request.data}")

        # Verifica se os dados estão no formato de uma lista de itens
        items = request.data.get('items', None)
        if items is None:
            # Se não for uma lista, tenta tratar como um único item
            single_item = request.data
            if 'product' in single_item and 'quantity' in single_item:
                items = [single_item]  # Converte para uma lista com um único item
            else:
                return Response({'success': False, 'message': 'Formato inválido ou nenhum item fornecido.'}, status=status.HTTP_400_BAD_REQUEST)

        # Processa os itens
        for item in items:
            if not isinstance(item, dict) or 'product' not in item or 'quantity' not in item:
                return Response({'success': False, 'message': 'Dados do item inválidos.'}, status=status.HTTP_400_BAD_REQUEST)
            
            try:
                product_id = int(item['product'])
                quantity = int(item['quantity'])
            except ValueError:
                return Response({'success': False, 'message': 'ID do produto e quantidade devem ser números inteiros.'}, status=status.HTTP_400_BAD_REQUEST)

            # Verifica se o usuário está autenticado
            user = request.user if request.user.is_authenticated else None

            # Cria o item no carrinho
            CartItem.objects.create(
                user=user,  # Associa ao usuário autenticado ou deixa como None
                product_id=product_id,
                quantity=quantity,
                is_active=True
            )
        
        return Response({'success': True, 'message': 'Itens adicionados ao carrinho com sucesso!'}, status=status.HTTP_201_CREATED)
    
    elif request.method == 'DELETE':
        # Limpa o carrinho
        if user:
            CartItem.objects.filter(user=user, is_active=True).delete()
        else:
            CartItem.objects.filter(user=None, is_active=True).delete()
        
        # Retorna uma resposta após a exclusão
        return Response({'success': True, 'message': 'Carrinho limpo com sucesso!'}, status=status.HTTP_204_NO_CONTENT)