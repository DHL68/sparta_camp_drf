from rest_framework import serializers
from user.models import User, UserProfile, Hobby
from blog.models import Article, Comment

# 게시글 정보 불러오기

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['content', 'updated_at']

class ArticleSerializer(serializers.ModelSerializer):

    comment = CommentSerializer(many=True)

    class Meta:
        model = Article
        # 게시글 정보 조회
        fields = ['user', 'title', 'content', 'category', 'updated_at', 'comment']


class HobbySerializer(serializers.ModelSerializer):

    # 이 기능을 통해 자신의 취미와 해당하는 유저 정보를 불러올 수 있음.
    # 자신이 원하는 메서드 필드 생성 가능
    same_hobby_users = serializers.SerializerMethodField()
    # SerializerMethodField() 를 사용하기 위해서는 get_same_hobby_users 꼭 필요
    def get_same_hobby_users(self, obj):
        # obj : hobby model 의 obj
        user_list = []
        for user_profile in obj.userprofile_set.all():
            user_list.append(user_profile.user.username)
        
        # return [up.user.username for up in obj.userprofile_set.all()] 축약식
        return user_list

    class Meta:
        model = Hobby
        fields = ['name', 'same_hobby_users']

class UserProfileSerializer(serializers.ModelSerializer):

    hobby = HobbySerializer(many=True) # input data queryset 일 경우

    class Meta:
        model = UserProfile
        # 불러오고자 하는 user 의 기본 정보와 상세 정보 불러오기
        fields = ['introduction', 'birthday', 'age', 'hobby']
        # __all__ 사용 방법도 있지만 사용하지 않는 이유는 불필요한 정보도 함께 불러오기 때문에
        # 특정 정보에 해당하는 정보만을 받기 위해서는 직접 설정해주는 것이 좋다.


class UserSerializer(serializers.ModelSerializer):

    # object 
    userprofile = UserProfileSerializer()

    # 해당 유저의 게시글 리스트
    userarticle = ArticleSerializer()
    
    class Meta:
        model = User
        # 역참조로 userprofile 정보 불러오기
        fields = ["username", "password", "fullname", "email", "join_date", "userprofile", "userarticle"]