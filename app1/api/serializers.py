from rest_framework import serializers
from app1.models import CustomUser, Advisor, Booking

# Advisor Serializer
class AdvisorSerializer(serializers.ModelSerializer):
    advisor_id = serializers.IntegerField(source='id',read_only=True)
    class Meta:
        model = Advisor
        fields = ['advisor_id','first_name','last_name','adv_photo']

# User Register Serializer
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True,write_only=True)
    password1 = serializers.CharField(required=True,write_only=True)
    class Meta:
        model = CustomUser
        fields = ['id','email','first_name','last_name','password','password1']
        extra_kwargs ={
            'password':{'write_only':True},
            'password1':{'write_only':True},
        }

    def create(self, validated_data):
        email = validated_data.get('email')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        password = validated_data.get('password')
        password1 = validated_data.get('password1')

        if password==password1:
            user = CustomUser(email=email,first_name=first_name,last_name=last_name)
            user.set_password(password)
            user.save()
            return user

        else:
            raise serializers.ValidationError(
                {'error': 'Both password do not match'}
            )

# Booking Serializer
class BookingSerializer(serializers.ModelSerializer):
    booking_id = serializers.IntegerField(source='id',read_only=True)
    advisor = AdvisorSerializer(read_only=True)
    class Meta:
        model = Booking
        fields = ['booking_id','booking_time','advisor',]

    

