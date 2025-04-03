
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('contato/', include('contato.urls')),
    path('servicos/', include('servicos.urls')),
    path('resultadoCotacao/', include('resultadoCotacao.urls')),
    path('planos/', include('planos.urls')),
]