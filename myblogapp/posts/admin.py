from django.contrib import admin

# Register your models here.

# 同じディレクトリのmodels.pyのclass Postから
from .models import Post

# admin.siteという管理サイトに追加する
admin.site.register(Post)
