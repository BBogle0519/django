
from django.db.models.functions.datetime import ExtractDay, ExtractWeek, ExtractWeekDay, ExtractYear
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import stepCount
from .serializers import StepCountSerializer

from django.db.models.aggregates import Sum
from django.db.models.functions import ExtractMonth

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


# 총 걸음수 확인(안드로이드에서 걸음 센서 기록값으로 처리했음)

# 걸음수 날짜별 확인(년, 월, 주)
@permission_classes([AllowAny])
@api_view(['POST'])
def StepStatisticsView(request):
    if request.method == 'POST':
        # print("[request.data]: " + str(request.data))
        if stepCount.objects.filter(user_id_pk=request.data['user_id_pk']).exists():
            year_data = stepCount.objects.annotate(year=ExtractYear('record')).values('year').annotate(step=Sum('step'), distance=Sum('distance')).values('year', 'step', 'distance').order_by('year')
            month_data = stepCount.objects.annotate(year=ExtractYear('record'), month=ExtractMonth('record')).values('year', 'month').annotate(step=Sum('step'), distance=Sum('distance')).values('year', 'month', 'step', 'distance').order_by('year', 'month')
            day_data = stepCount.objects.annotate(year=ExtractYear('record'), month=ExtractMonth('record'), day=ExtractDay('record')).values('year', 'month', 'day').annotate(step=Sum('step', distance=Sum('distance'))).values('year', 'month', 'day', 'step', 'distance').order_by('year', 'month', 'day')

            # print("[year_data]: " + str(year_data))
            # print("[month_data]: " + str(month_data))
            # print("[day_data]: " + str(day_data))

            data = {
                'message' : 'ok',
                'year_data' : year_data,
                'month_data' : month_data,
                'day_data' : day_data,
            }
            # print("[data]: " + str(data))

            return Response(data, status=status.HTTP_200_OK)

        else :
            data ={
                'message' : 'DoesNotExist',
            }

            return Response(data, status=status.HTTP_400_BAD_REQUEST)
            
