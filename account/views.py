from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from .models import User_Tb
from .serializers import JoinSerializer, LoginSerializer, UserSerializer

# import bcrypt

# Create your views here.


@permission_classes([AllowAny])
class JoinViewSet(viewsets.ModelViewSet):
    queryset = User_Tb.objects.all()
    serializer_class = JoinSerializer

    def create(self, request, *args, **kwargs):
       # print("[request.data]: " + str(request.data))

        # 사용자 비밀번호 암호화하여 저장
        # pw = request.data['password'].encode('utf-8')
        # pw_crypt = bcrypt.hashpw(pw, bcrypt.gensalt())
        # pw_crypt = pw_crypt.decode('utf-8')

        # request.data value를 변경할 때 immutable 에러 발생하여 copy() 이용하여 변경
        # request_cp = request.data.copy()
        # request_cp['password'] = pw_crypt
        # print("request_cp " + str(request_cp))

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save() 


@api_view(['POST'])
@permission_classes([AllowAny])
def LoginView(request):
    if request.method == 'POST':
        # print("[request.data]: " + str(request.data))
        try:
            user = User_Tb.objects.get(user_id=request.data.get('user_id'))
            # serializer = LoginSerializer(data=request.data)
            # print("query user: " + str(user))

            # authenticate(request=None, **credentials) 장고 제공 인증 함수
            if (authenticate(user_id=request.data.get('user_id'), password=request.data.get('password'))):
                token = RefreshToken.for_user(user)
                data = {
                    'refresh': str(token),
                    'access': str(token.access_token),
                }
                # print("token result: " + str(token))
                return Response(data, status=status.HTTP_200_OK)

            # if bcrypt.checkpw(request.data['password'].encode('utf-8'), user.password.encode('utf-8')):
            #     token = RefreshToken.for_user(user)
            #     data = {
            #         'refresh': str(token),
            #         'access': str(token.access_token),
            #     }
            #     print("token result: " + str(token))
            #     return Response(data, status=status.HTTP_200_OK)

            return Response(status=status.HTTP_400_BAD_REQUEST)

        except User_Tb.DoesNotExist:
            # print("잘못된 user_id 입력")
            return Response(status=status.HTTP_400_BAD_REQUEST)

        except User_Tb.MultipleObjectsReturned:
            # print("테이블에 user_id unique로 박혀있어서 여기 올일은 없음")
            return Response(status=status.HTTP_400_BAD_REQUEST)

# postman에서 토큰 테스트용 api
class UserViewSet(viewsets.ModelViewSet):
    queryset = User_Tb.objects.all()
    serializer_class = UserSerializer