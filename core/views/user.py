from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import User
from core.serializers.user import UserSerializer
from django.http import Http404
from drf_yasg.utils import swagger_auto_schema

class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    

    @swagger_auto_schema(request_body=UserSerializer)
    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserGetOrCreateByUid(APIView):
    
    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        uid = request.data.get('uid')

        if not uid:
            return Response({"error": "UID parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(uid=uid)
            created = False
        except User.DoesNotExist:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                user = serializer.instance
                created = True
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        if created:
            return Response({"message": "User created successfully", "user": UserSerializer(user).data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "User already exists", "user": UserSerializer(user).data}, status=status.HTTP_200_OK)
