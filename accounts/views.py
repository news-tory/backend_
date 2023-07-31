from .models import CustomUser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer, SignupSerializer
from django.contrib import auth
from django.contrib.auth.hashers import make_password

@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data) # serializer에서 데이터 받음
    if serializer.is_valid():                       # 유효성 검사. 받아온 데이터가 문제 없다면,
        user = auth.authenticate(                   # auth.authenticate를 사용해 유저 반환
            request=request,
            username=serializer.data['username'],
            password=serializer.data['password'],
        )
        if user is not None:
            auth.login(request, user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def signup(request):
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        new_user = serializer.save(password = make_password(serializer.validated_data['password']))
        # make_password: 문자열로 받은 패스워드를 해시값으로 변경해주는 역할
        auth.login(request, new_user)
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logout(request):
    auth.logout(request)
    return Response(status=status.HTTP_200_OK)