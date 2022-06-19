from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from blog.models import Article

from rest_framework import status

from user.serializers import ArticleSerializer

# Create your views here.

class ArticleView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        user = request.user

        articles = Article.objects.filter(user=user)
        # title = [article.title for article in articles] # list 축약 문법

        titles = []

        for article in articles:
            titles.append(article.title)

        return Response({"article_list": titles})