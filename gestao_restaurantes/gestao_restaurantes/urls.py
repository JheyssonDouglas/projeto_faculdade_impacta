from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect  # Import necessário para o redirecionamento

def redirect_to_products(request):
    return redirect('/api/products/')  # Redireciona para a API de produtos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('restaurante.urls')),  # Inclui as URLs do app restaurante
    path('', redirect_to_products),  # Redireciona a raiz para /api/products/
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
