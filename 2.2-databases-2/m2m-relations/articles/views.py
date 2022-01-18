from django.shortcuts import render
from .models import Article, Scope, ArticleScope


def articles_list(request):
    template = 'articles/news.html'
    context = {'articles': Article.objects.order_by('-published_at').all()}

    return render(request, template, context)
