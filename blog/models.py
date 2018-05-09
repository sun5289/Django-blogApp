from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')   # 글작성자
    title = models.CharField(max_length=255)    # 제목
    text = models.TextField()                  # 글 내용
    #test = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)  # 글작성일자
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return  self.title


