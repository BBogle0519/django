from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import stepCount
from .serializers import StepCountSerializer

# Create your views here.

# 측정된 걸음수 저장
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

        return Response(serializer.data, status=status.HTTP_200_OK)


# 총 걸음수 확인(안드로이드센서에서 처리했음)
# 걸음수 날짜별 확인(년, 월, 주)
@permission_classes([AllowAny])
@api_view(['POST'])
def StepStatistics(request):
    if request.method == 'POST':
        #if request == 년도별
        #data = fitter (request=사용자 id, 연별로 묶은step수)
        #return Response(data,status=status.HTTP_200_OK)

        #else if request == 월별
        #data = fitter (request=사용자 id, 월별로 묶은step수)
        #return Response(data,status=status.HTTP_200_OK)

        #else if request == 주별
        #data = fitter (request=사용자 id, 주별로 묶은step수)
        #return Response(data,status=status.HTTP_200_OK)

        #-------------or------------
        # 한번에 년월주 데이터 response
        # year = fitter (request=사용자 id, 연별로 묶은step수)
        # month = ...
        # week = ...

        # data= {'년': year, '월' : month, '주' : week}

        #return Response(data,status=status.HTTP_200_OK)
        pass
        