from rest_framework import generics
from access.models import Profile, Company
from api.serializers import ProfileSerializer, CompanySerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from api.permissions import ProfilePermissionClass
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets, generics
from access.models import Profile, Company
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from drf_spectacular.utils import extend_schema, OpenApiResponse

# Profile Views
class ProfileCreateListAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    @extend_schema(
        responses={
            200: ProfileSerializer,  # Sucesso ao listar
            201: ProfileSerializer,  # Sucesso ao criar
            400: OpenApiResponse(description="Bad Request"),  # Erro de requisição
            500: OpenApiResponse(description="Internal Server Error")  # Erro no servidor
        },
        description="Criação e listagem de perfis. Esta rota permite criar um novo perfil ou listar os perfis existentes.",
        operation_id="ProfileList",
        tags=["Profiles"]  # Definindo a categoria para Swagger
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
            responses={
            201: ProfileSerializer,  # Sucesso ao criar
            400: OpenApiResponse(description="Bad Request"),
            500: OpenApiResponse(description="Internal Server Error")
        },
        description="Criação de um novo perfil. Envia os dados necessários para criar um perfil.",
        operation_id="ProfileCreate",
        tags=["Profiles"]  # Definindo a categoria para Swagger
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class ProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    @extend_schema(
        description="Recuperação, atualização e destruição de um perfil existente.",
        operation_id="ProfileDetail",
        tags=["Profiles"]  # Definindo a categoria para Swagger
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        description="Atualização de todos os dados de um perfil existente.",
        operation_id="ProfileUpdateAll",
        tags=["Profiles"]  # Definindo a categoria para Swagger
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    @extend_schema(
        description="Atualização de dados de uma empresa existente.",
        operation_id="ProfileUpdate",
        tags=["Profiles"]  # Definindo a categoria para Swagger
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        description="Deletar um perfil existente.",
        operation_id="ProfileDelete",
        tags=["Profiles"]  # Definindo a categoria para Swagger
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

# Company Views
class CompanyCreateListAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @extend_schema(
        description="Criação e listagem de empresas. Esta rota permite criar uma nova empresa ou listar as empresas existentes.",
        operation_id="CompanyList",
        tags=["Companies"]  # Definindo a categoria para Swagger
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        description="Criação de uma nova empresa. Envia os dados necessários para criar uma empresa.",
        operation_id="CompanyCreate",
        tags=["Companies"]  # Definindo a categoria para Swagger
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class CompanyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @extend_schema(
        description="Recuperação, atualização e destruição de uma empresa existente.",
        operation_id="CompanyDetail",
        tags=["Companies"]  # Definindo a categoria para Swagger
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        description="Atualização de todos os dados de uma empresa existente.",
        operation_id="CompanyUpdateAll",
        tags=["Companies"]  # Definindo a categoria para Swagger
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    @extend_schema(
        description="Atualização de dados de uma empresa existente.",
        operation_id="CompanyUpdate",
        tags=["Companies"]  # Definindo a categoria para Swagger
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        description="Deletar uma empresa existente.",
        operation_id="CompanyDelete",
        tags=["Companies"]  # Definindo a categoria para Swagger
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    

# Adicionando tags na autenticação (Token, Refresh, Verify)
class CustomTokenObtainPairView(TokenObtainPairView):
    @extend_schema(
        tags=["Authentication"],  # Definindo a tag "Authentication"
        description="Obtém o token JWT para autenticação"
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CustomTokenRefreshView(TokenRefreshView):
    @extend_schema(
        tags=["Authentication"],  # Definindo a tag "Authentication"
        description="Atualiza o token JWT"
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CustomTokenVerifyView(TokenVerifyView):
    @extend_schema(
        tags=["Authentication"],  # Definindo a tag "Authentication"
        description="Verifica a validade do token JWT"
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
# # ViewSets para Profile e Company

# class ProfileViewSet(viewsets.ModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [IsAuthenticated]

#     @extend_schema(
#         description="Listagem, criação, detalhamento, atualização e exclusão de perfis.",
#         operation_id="ProfileViewSet"
#     )
#     def list(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)

#     @extend_schema(
#         description="Criação de um novo perfil. Envia os dados necessários para criar um perfil.",
#         operation_id="ProfileCreate"
#     )
#     def create(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)

#     @extend_schema(
#         description="Detalha um perfil existente.",
#         operation_id="ProfileDetail"
#     )
#     def retrieve(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)

#     @extend_schema(
#         description="Atualiza os dados de um perfil existente.",
#         operation_id="ProfileUpdate"
#     )
#     def update(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)

#     @extend_schema(
#         description="Deleta um perfil existente.",
#         operation_id="ProfileDelete"
#     )
#     def destroy(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)


# class CompanyViewSet(viewsets.ModelViewSet):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer
#     permission_classes = [IsAuthenticated]

#     @extend_schema(
#         description="Listagem, criação, detalhamento, atualização e exclusão de empresas.",
#         operation_id="CompanyViewSet"
#     )
#     def list(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)

#     @extend_schema(
#         description="Criação de uma nova empresa. Envia os dados necessários para criar uma empresa.",
#         operation_id="CompanyCreate"
#     )
#     def create(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)

#     @extend_schema(
#         description="Detalha uma empresa existente.",
#         operation_id="CompanyDetail"
#     )
#     def retrieve(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)

#     @extend_schema(
#         description="Atualiza os dados de uma empresa existente.",
#         operation_id="CompanyUpdate"
#     )
#     def update(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)

#     @extend_schema(
#         description="Deleta uma empresa existente.",
#         operation_id="CompanyDelete"
#     )
#     def destroy(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)


