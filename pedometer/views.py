from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import stepCount
from .serializers import StepCountSerializer

# Create your views here.


@permission_classes([AllowAny])
class StepCountViewSet(viewsets.ModelViewSet):
    queryset = stepCount.objects.all()
    serializer_class = StepCountSerializer

    def create(self, request, *args, **kwargs):
        print("[request.data]: " + str(request.data))

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
