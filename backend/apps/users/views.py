from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from .models import Profile as User


class UserListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        users = get_list_or_404(User)
        serializer = serializers.UserSerializer(
            users,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.UserDetailSerializer(
            data=request.data,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class UserDetailView(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = serializers.UserDetailSerializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        if user:
            serializer = serializers.UserDetailSerializer(
                user,
                data=request.data,
            )
            serializer.is_valid(raise_exception=True)

            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        if "password" in request.data:
            return Response(
                "You cannot update your passowrd."
                + f" Use endpoint url /api/{pk}/change-passowrd/ ",
                status=status.HTTP_204_NO_CONTENT,
            )
        if "email" in request.data:
            return Response(
                "You cannot update your email."
                + f"Use endpoint url /api/{pk}/change-email/ ",
                status=status.HTTP_204_NO_CONTENT,
            )

        user = get_object_or_404(User, pk=pk)

        if user:
            serializer = serializers.UserSerializer(
                user, data=request.data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response("User is deleted.", status=status.HTTP_200_OK)


class RankingListView(APIView):
    def get(self, request):
        users = User.objects.filter_by_total_score()
        serializer = serializers.RankingSerializer(users, many=True)
        serializer_data = serializer.data
        for position, user in enumerate(serializer_data, start=1):
            user["rank"] = position
        return Response(serializer_data)


class ChangePasswordView(APIView):
    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = serializers.ChangePasswordSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            old_password = serializer.data.get("old_password")
            new_password = serializer.data.get("new_password")
            print(old_password, new_password)
            if not user.check_password(raw_password=old_password):
                return Response(
                    ({"old_password": "Wrong password.."}),
                    status=status.HTTP_400_BAD_REQUEST,
                )

            user.set_password(new_password)
            user.save()
            return Response(
                "Password is succesfully updated.",
                status=status.HTTP_206_PARTIAL_CONTENT,
            )
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class ScoreUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = serializers.ScoreUserSerializer(user)
        return Response(serializer.data)


class ScoreAdderView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = serializers.ScoreAdderSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
