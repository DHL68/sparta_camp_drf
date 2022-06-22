from unicodedata import category
from rest_framework import serializers
from blog.models import Article as ArticleModel
from blog.models import Comment as CommentModel
from blog.models import Category as CategoryModel

# 게시글 정보 불러오기

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryModel
        fields = ['name']


class CommentSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = CommentModel
        fields = ['user' ,'content']

class ArticleSerializer(serializers.ModelSerializer):

    comment = CommentSerializer(many=True, source="comment_set")

    # 어떤 카테고리에 해당하는지 이름 정보 불러오기
    # .SerializerMethodField() 함수를 사용하기 위해
    category = serializers.SerializerMethodField()

    # get_이름 의 함수를 정의 한다.
    def get_category(self, obj):
        # 축약식을 활용해서 카테고리의 정보를 카테고리 안에 담는다.
        return [category.name for category in obj.category.all()]

    class Meta:
        model = ArticleModel
        # 게시글 정보 조회
        fields = ['user', 'title', 'content', 'category', 'exposure_start', 'exposure_end', 'comment', 'category']