from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

class RegisterView(APIView):
    def post(self, request):
        data = request.data
        mandatory_fields = ['email', 'name', 'mobile_number', 'city', 'password']
        for field in mandatory_fields:
            if field not in data:
                return Response({"error": f"{field} is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Handle referral code logic
        referrer = None
        if 'referral_code' in data:
            try:
                referrer = User.objects.get(referral_code=data['referral_code'])
            except User.DoesNotExist:
                return Response({"error": "Invalid referral code."}, status=status.HTTP_400_BAD_REQUEST)

        # Create user
        user = User.objects.create(
            email=data['email'],
            name=data['name'],
            mobile_number=data['mobile_number'],
            city=data['city'],
            password=data['password'],  # Use hashed passwords in real-world apps
            referrer=referrer
        )
        return Response({"message": "User registered successfully!", "referral_code": user.referral_code})

class LoginView(APIView):
    def post(self, request):
        data = request.data
        email = data.get('email')
        password = data.get('password')

        try:
            user = User.objects.get(email=email)
            if user.password == password:  # Use hashed password comparison in real-world apps
                return Response({"user_id": user.id, "email": user.email})
            return Response({"error": "Invalid password."}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

class ReferralView(APIView):
    def get(self, request, referral_code):
        try:
            user = User.objects.get(referral_code=referral_code)
            referees = user.referees.all().values('name', 'email', 'registration_date')
            return Response(referees)
        except User.DoesNotExist:
            return Response({"error": "Invalid referral code."}, status=status.HTTP_404_NOT_FOUND)
