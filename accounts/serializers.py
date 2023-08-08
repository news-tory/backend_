from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):  # 회원가입 & 로그인 똑같은 시리얼라이저 사용 (create 오버라이딩 유무만 차이)
    class Meta:
<<<<<<< HEAD
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
=======
        model = User
        fields = '__all__'

    # 유효성 검증을 통과한 값인 validated_data을 이용해서 입력값을 검증하고 유저객체 생성
    def create(self, validated_data):
        user = User.objects.create_user(
            nickname = validated_data['nickname'],
            email = validated_data['email'],
            password = validated_data['password']
        )
        return user
>>>>>>> 807a25ec25b30158713234bd35b391b560f3d99b
