from django.db import models
from datetime import timezone
from django.utils import timezone

# Create your models here.

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey('user.User', verbose_name="작성자", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="제목", max_length=50)
    thumbnail = models.FileField("썸네일", upload_to="product/")
    description = models.TextField("설명")
    created = models.DateTimeField("등록일자", auto_now_add=True)
    exposure_start_date = models.DateField("노출 시작 일", default=timezone.now)
    exposure_end_date = models.DateField("노출 종료 일", default=timezone.now)

    def __str__(self):
        return f"제목 : {self.title}"