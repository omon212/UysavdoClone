from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from drf_yasg.utils import swagger_auto_schema
from Users.models import UsersModel
from Users.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class RegisterUser(APIView):
    serializer_class = UserSerializer
    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        # serializer = UserSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=201)
        # return Response(serializer.errors, status=400)
        phone = request.data.get("phone")
        user = UsersModel.objects.filter(phone=phone).exists()
        if user:
            return Response({"detail": "Siz allaqachon ro'yxatdan o'tgansiz"}, status=400)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


from .models import UsersModel

class LoginUser(APIView):
    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        phone = request.data.get("phone")

        user = UsersModel.objects.filter(phone=phone).first()

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }, status=200)
        else:
           return Response({"detail": "Telefon raqami noto‘g‘ri yoki mavjud emas"}, status=401)

class Getusers(APIView):
    def get(self, request):
        users = UsersModel.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class DeleteUser(APIView):
    serializer_class = UserSerializer

    @swagger_auto_schema(request_body=UserSerializer)
    def delete(self, request):
        phone = request.data.get("phone")
        try:
            # Try to retrieve the user based on the provided phone
            user = UsersModel.objects.get(phone=phone)
        except UsersModel.DoesNotExist:
            # Return a response if the user does not exist
            return Response(
                {"detail": "User not found"},
                status=404
            )

        # Delete the user if found
        user.delete()
        return Response(
            {"detail": "User deleted successfully"},
            status=200
        )

