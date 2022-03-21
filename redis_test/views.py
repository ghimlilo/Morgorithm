from cgitb import text
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from .models import Post


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

@cache_page(CACHE_TTL)
def home(request):
    text = 'hello world'
    return render(request, 'redis_test/home.html', {'text':text})


# def my_view(request):
#     posts = Post.objects.all().values('id', 'text')
#     return JsonResponse(list(posts), safe=False)

def my_view(request):
    posts = cache.get_or_set('posts', Post.objects.all().values('id', 'text'))
    return JsonResponse(list(posts), safe=False)


