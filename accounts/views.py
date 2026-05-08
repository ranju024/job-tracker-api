from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
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


