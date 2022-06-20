from rest_framework import serializers
from blog.models import Article, Comment, Category

# 게시글 정보 불러오기

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['content', 'updated_at']

class ArticleSerializer(serializers.ModelSerializer):

    comment = CommentSerializer(many=True, source="comment_set")

    # 어떤 카테고리에 해당하는지 이름 정보 불러오기
    category = CategorySerializer(many=True)

    class Meta:
        model = Article
        # 게시글 정보 조회
        fields = ['user', 'title', 'content', 'category', 'updated_at', 'comment', 'category']