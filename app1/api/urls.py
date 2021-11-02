from django.urls import path,include
from app1.api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router = DefaultRouter()


urlpatterns = [
    
    path('admin/advisor/', views.AdvisorView.as_view(),name='advisor'),
    path('user/register/', views.UserRegisterAPIView.as_view(), name='register'),
    path('user/login', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/<int:user_id>/advisor/', views.AdvisorsDetailsView.as_view(), name='advisor_details'),
    path('user/<int:user_id>/advisor/<int:advisor_id>/', views.BookingView.as_view(),name='advisor_call_booking'),
    path('user/<int:user_id>/advisor/booking/', views.BookingDetailsView.as_view(),name='booking_details'),

]
