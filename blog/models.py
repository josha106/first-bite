from django.db import models

# models.Module의 상속받음
class Post(models.Model):
  #문자를 담는 필드, 최대 길이 30
  title = models.CharField(max_length=30)
  #길이의 제한이 없는 문자열
  content = models.TextField()
  #월, 일, 시, 분, 초를 담는 필드
  created_at = models.DateTimeField()
  #author: 추후 작성 예정