from rest_framework import serializers
from access.models import Profile, Company
from django.contrib.auth.models import User

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# class ProfileSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Profile
#         fields = '__all__'

# class CompanySerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Company
#         fields = '__all__'
