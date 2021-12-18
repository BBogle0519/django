from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# router를 필수로 사용해야하는건 아님. url 깔끔하게 정리하는 용도로 생각
router = routers.DefaultRouter()
router.register('Join', views.JoinViewSet, basename = "Join")
# router.register('Login', views.LoginUser, basename = "LoginUser")

urlpatterns = [
    path('', include(router.urls)),
    path('Login/', views.LoginView, name='Login'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view()),
]
