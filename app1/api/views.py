from app1.models import Advisor, Booking
from .serializers import AdvisorSerializer,BookingSerializer,UserRegisterSerializer
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

# Add Advisor
class AdvisorView(CreateAPIView):    
    serializer_class = AdvisorSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

# User Registration 
class UserRegisterAPIView(CreateAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            response_data = {
                'userid': serializer.data['id'],
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(response_data, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

# Advisor Details
class AdvisorsDetailsView(ListAPIView):
    queryset = Advisor.objects.all()
    serializer_class = AdvisorSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
# Book call with an Advisor
class BookingView(CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def post(self, request, format=None, *args, **kwargs):
        user_id = self.kwargs['user_id']
        advisor_id = self.kwargs['advisor_id']
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(customuser_id=user_id, advisor_id=advisor_id)
            return Response(status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

# Get all booked calls
class BookingDetailsView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['user_id']
        data = Booking.objects.filter(customuser=pk)
        return data
