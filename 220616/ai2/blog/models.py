from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField("사용자 이름", max_length=50)
    description = models.TextField("설명")

    def __str__(self):
        return self.name

class Article(models.Model):
    user = models.ForeignKey('user.User', verbose_name="글 작성자", on_delete=models.CASCADE)
    title = models.CharField("글 제목", max_length=50)
    content = models.TextField("글 본문")
    category = models.ManyToManyField(Category, verbose_name="카테고리")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} 님이 작성하신 글입니다."

class Comment(models.Model):
    # Article 에 작성한 코멘트의 출처(작성자) / CASCADE 댓글의 작성자 데이터가 없는 경우 함께 댓글 데이터 삭제 설정
    user = models.ForeignKey('user.User', verbose_name="댓글 작성자", on_delete=models.CASCADE)
    # Article 과의 댓글 관계 정의 / CASCADE 게시글 데이터가 없는 경우 함께 댓글 데이터 삭제 설정
    article = models.ForeignKey(Article, verbose_name="댓글을 작성한 글", on_delete=models.CASCADE)
    content = models.TextField("댓글 내용")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} 님이 작성하신 댓글입니다."
