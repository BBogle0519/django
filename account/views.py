from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User_Tb
from .serializers import JoinSerializer, LoginSerializer

# Create your views here.


class JoinViewSet(viewsets.ModelViewSet):
    queryset = User_Tb.objects.all()
    serializer_class = JoinSerializer

    def create(self, request, *args, **kwargs):
        print("[request.data]: " + str(request.data))

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def LoginView(request):
    if request.method == 'POST':
        print ("[request.data]: " + str(request.data))