from turtle import st
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from blog.models import Article as ArticleModel
from rest_framework import status

from ai.permissions import IsAdminOrAuthenticatedReadOnly

from blog.serializers import ArticleSerializer

from django.utils import timezone

# Create your views here.

class ArticleView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.AllowAny]

    permission_classes = [IsAdminOrAuthenticatedReadOnly]   # 커스텀 permissions

    def get(self, request):
        user = request.user
        today = timezone.now()
        articles = ArticleModel.objects.filter(
            exposure_start__lte = today,
            exposure_end__gte = today,
        ).order_by("-id")

        serializer = ArticleSerializer(articles, many=True).data

        # titles = [article.title for article in articles] # list 축약 문법

        # titles = []

        # for article in articles:
        #     titles.append(article.title)

        return Response(serializer, status=status.HTTP_200_OK)

    # 글 생성 기능 구현
    def post(self, request):
        user = request.user
        title = request.data.get("title", "")
        contents = request.data.get("content", "")
        category = request.data.pop("category", [])

        # 글자수 조건 이하일 경우
        if len(title) <= 5:
            return Response({"error" : "타이틀은 5자 이상 작성하셔야 합니다."}, status=status.HTTP_400_BAD_REQUEST)
        
        # 글자수 조건 이하일 경우
        if len(contents) <= 20:
            return Response({"error" : "글 내용은 20자 이상 작성하셔야 합니다."}, status=status.HTTP_400_BAD_REQUEST)
        
        if not category:
            return Response({"error" : "카테고리가 지정되지 않았습니다."}, status=status.HTTP_400_BAD_REQUEST)

        article = ArticleModel(
            user = user,
            # kwarge 를 사용하기 위해 같은 ManyToMany 의 카테고리를 .pop 으로 카테고리를 request 데이터에서 제외시킨다.
            **request.data
        )
        article.save()
        article.category.add(*category)
        return Response({"message": "성공!"}, status=status.HTTP_200_OK)