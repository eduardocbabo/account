from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from access.views import base, lista_usuarios
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.permissions import IsAuthenticated
from rest_framework.routers import DefaultRouter
# from api.views import ProfileViewSet, CompanyViewSet
from api.views import ProfileCreateListAPIView, ProfileRetrieveUpdateDestroyAPIView, CompanyCreateListAPIView, CompanyRetrieveUpdateDestroyAPIView
from api.views import CustomTokenObtainPairView, CustomTokenRefreshView, CustomTokenVerifyView
# Configuração para Swagger com JWT
swagger_ui_parameters = {
    'defaultModelsExpandDepth': -1,
    'defaultModelRendering': 'model'
}


# Criação de um roteador para gerenciar automaticamente as URLs
# router = DefaultRouter()
# router.register(r'profiles', ProfileViewSet)
# router.register(r'companies', CompanyViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', base, name='base'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # Para login no DRF
    
    # Incluir suas URLs do aplicativo 'api'
    path('access/', include('access.urls')),
    
    # Endpoints de autenticação
    path('api/v1/auth/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/auth/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/auth/token/verify/', CustomTokenVerifyView.as_view(), name='token_verify'),

    # Rota para a geração do schema (OpenAPI)
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),

    # Rota para a UI do Swagger, usando o schema gerado
    path('api/v1/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'), name='api-docs'),
    
    # Rotas para o perfil
    path('api/v1/profiles/', ProfileCreateListAPIView.as_view(), name='profile-create-list'),
    path('api/v1/profiles/<int:pk>/', ProfileRetrieveUpdateDestroyAPIView.as_view(), name='profile-detail'),

    # Rotas para a empresa
    path('api/v1/companies/', CompanyCreateListAPIView.as_view(), name='company-create-list'),
    path('api/v1/companies/<int:pk>/', CompanyRetrieveUpdateDestroyAPIView.as_view(), name='company-detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



# """
# URL configuration for mesa project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.1/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from access.views import base, lista_usuarios
# from django.contrib.auth.models import User
# from rest_framework import routers, serializers, viewsets, generics
# from access.models import Profile, Company
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# # Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']

# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class ProfileSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Profile
#         fields = '__all__'

# # ViewSets define the view behavior.
# class ProfileViewSet(viewsets.ModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer

# class CompanySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Company
#         fields = '__all__'

# # ViewSets define the view behavior.
# class CompanyViewSet(viewsets.ModelViewSet):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer

# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'profiles', ProfileViewSet)
# router.register(r'companys', CompanyViewSet)

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#     # path('', base, name='base'),
#     path('access/', include('access.urls')),
#     path('usuarios/', lista_usuarios, name='lista_usuarios'),
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
#     path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
#     path('api/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'), name='api-docs'),
    
# ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

