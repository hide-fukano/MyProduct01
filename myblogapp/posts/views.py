from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Hello, Wolrd! このページは投稿のインデックスです")
    return render(request, 'posts/index.html')

# Create your views here.
