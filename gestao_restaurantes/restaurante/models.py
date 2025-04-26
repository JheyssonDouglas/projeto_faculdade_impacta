from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    category = models.CharField(max_length=100, default="")  
    subcategory = models.CharField(max_length=100, default="")  

    def __str__(self):
        return self.name

class CustomUserManager(BaseUserManager):
    def create_user(self, email, nome, password=None):
        if not email:
            raise ValueError('O usuário deve ter um email')
        if not nome:
            raise ValueError('O usuário deve ter um nome')

        user = self.model(
            email=self.normalize_email(email),
            nome=nome,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, password=None):
        user = self.create_user(
            email,
            nome=nome,
            password=password,
        )
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    def __str__(self):
        return self.email
    
class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart_items', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)  # Indica se o item está ativo no carrinho

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.quantity}x {self.product.name} ({self.user.email if self.user else 'Anônimo'})"