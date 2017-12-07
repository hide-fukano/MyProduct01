from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    published = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()

    # __str__で文字列をページに返してくれる
    def __str__(self):
        # titleの文字列を返す
        return self.title

    # 先頭から100文字分だけ文章だけを返す
    def summary(self):
        return self.body[:100]
