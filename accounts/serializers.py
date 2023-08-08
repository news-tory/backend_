from rest_framework import serializers
from .models import CustomUser

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128)
    
class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'nickname', 'university', 'location']

# 이미지 등록, 변경
# class ProfileImgSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['profile_img']

# 닉네임 변경
# class NicknameSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['nickname']

# # 비밀번호 변경
# class PasswordSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['password']
        
# # 선호하는 카테고리 수정
# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['category']