import json

from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from .models import CustomUser
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializer import CustomUserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser


class SignIn(APIView):
    def post(self, request):
        data = json.loads(request.body)
        user = authenticate(username=data.get("username"), password=data.get("password"))
        if user:
            serializer_user = CustomUserSerializer(user)
            return Response(serializer_user.data)
        return JsonResponse({'message': 'Unsuccessfully!'})


class UserApiView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserApiUpdate(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class UserApiDestroy(generics.RetrieveDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = (IsAdminOrReadOnly, )


# class UserApiViewSet(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer

# class UserSingleApiView(APIView):
#
#     def get_object(self, id):
#         try:
#             user = CustomUser.objects.get(id=id)
#             return user
#         except CustomUser.DoesNotExist:
#             return None
#
#     def get(self, request, pk):
#         user = self.get_object(pk)
#         if not user:
#             return Response({"error": f"Does not exist User with id: {pk}"})
#         serializer_user = CustomUserSerializer(user)
#         return Response(serializer_user.data)
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#         user = self.get_object(pk)
#         if not user:
#             return Response({"error": f"Does not exist User with id: {pk}"})
#         serializer = CustomUserSerializer(data=request.data, instance=user)
#         serializer.is_valid()
#         serializer.save()
#         return Response({'user': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#         # здесь удаление записи или сделать юзера не активным
#         user = self.get_object(pk)
#         if user:
#             user.is_active = False
#             serializer = CustomUserSerializer(instance=user, data={'is_active': False})
#             serializer.is_valid()
#             serializer.save()
#         return Response({'user': "deleted User " + str(pk)})
#
#
# class UserApiView(generics.ListCreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer

# class UserApiView(APIView):
# #полностью этот функионал выполняет generics.ListCreateAPIView из DRF. Задать queryset=CustomUser.objects.all() и serializer =... .
#     def get(self, request):
#         queryset = CustomUser.objects.all()
#         serializer_users = CustomUserSerializer(queryset, many=True)
#         return Response(serializer_users.data)
#
#     def post(self, request):
#         serializer = CustomUserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'user': serializer.data})



# @csrf_exempt
# def sign_in(request):
#     print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#     print('Є КОНТАКТ')
#     print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#
#     if request.method == "POST":
#         print(request.POST)
#         print(json.loads(request.body))
#         data = json.loads(request.body)
#         user = authenticate(username=data.get("username"), password=data.get("password"))
#         if user:
#             login(request, user)
#             # next_page = request.POST.get('next')
#             # if next_page:
#             #     return redirect(next_page)
#             return JsonResponse({'message': 'Successfully!'})
#         return JsonResponse({'message': 'Unsuccessfully!'})
#     return JsonResponse({'message': 'Waiting for POST with user data!'})
#
