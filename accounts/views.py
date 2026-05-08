from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer

# Create your views here.
class RegisterView(APIView):
    permission_classes = [AllowAny]  # anyone can register without token; overrides the global IsAuthenticated setting.

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            # Django will raise an AssertionError if u don't call is_valid() before save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# u need to blacklist the refresh token once the user logs out   
class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data['refresh']  # gets the refresh token from the request body
            token = RefreshToken(refresh_token)  # creates a RefreshToken object from the raw token string so simplejwt can work with it
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST) 




