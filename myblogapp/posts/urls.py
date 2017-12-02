from django.conf.urls import url

# 同じ階層のviews.pyを読み込みなさい
from . import views

urlpatterns = [url(r'^$',views.index, name='index')]
