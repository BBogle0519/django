from rest_framework import serializers
from .models import User_Tb


# 회원가입
class JoinSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User_Tb.objects.create_user(
            user_id=validated_data['user_id'],
            password=validated_data['password'],
            user_nm=validated_data['user_nm'],
            user_ph=validated_data['user_ph'],
            user_email=validated_data['user_email'],
        )

        return user

    class Meta:
        model = User_Tb
        fields = ('user_id', 'password', 'user_nm',
                  'user_ph', 'user_email',)

# 로그인


class LoginSerializer(serializers.ModelSerializer):
    # def validate(self, data):
    #     userid = data.get("user_id", None)
    #     password = data.get("password", None)
    #     user = authenticate(user_id=user_id, password=password)

    #     return user

    class Meta:
        model = User_Tb
        fields = ('id', 'user_id', 'password',)


# 토큰 테스트용
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Tb
        fields = "__all__"
