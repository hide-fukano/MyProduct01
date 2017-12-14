from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# 同じディレクトリのmodelsからPostを取得
from .models import Post


def index(request):
    # Post.objectsはPostから全てのデータを取ってきますよの意
    # postsという変数に公開日の降順でソートする(piblished)
    posts = Post.objects.order_by('-published')
    # return HttpResponse("Hello, Wolrd! このページは投稿のインデックスです")
    # {'テンプレ内での変数名': 渡す変数名（上で作った配列posts）}
    return render(request, 'posts/index.html', {'posts': posts})

def post_detail(request,post_id):
    post = get_object_or_404(Post,pk=post_id)
    return render(request, 'posts/post_detail.html',{'post':post})

# Create your views here.
