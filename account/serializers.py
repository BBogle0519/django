from django.db.models import fields
from rest_framework import serializers
from .models import User_Tb

# 회원가입
class JoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Tb
        fields = ('user_id', 'user_pw', 'user_nm',
                  'user_ph', 'user_email',)

# 로그인
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Tb
        fields = ('id', 'user_id', 'user_pw',)
