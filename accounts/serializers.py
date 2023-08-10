from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):  # 회원가입 & 로그인 똑같은 시리얼라이저 사용 (create 오버라이딩 유무만 차이)
    class Meta:
        model = User
        fields = "__all__"

    # 유효성 검증을 통과한 값인 validated_data을 이용해서 입력값을 검증하고 유저객체 생성
    def create(self, validated_data):
        user = User.objects.create_user(
            # nickname = validated_data['nickname'],
            # email = validated_data['email'],
            # password = validated_data['password'],
            # sport = validated_data['sport'],
            **validated_data
        )
        return user
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance