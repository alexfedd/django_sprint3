from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category


def index(request):
    """Главная страница: отображает 5 последних публикаций."""
    posts = Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')[:5]
    return render(request, 'blog/index.html', {'post_list': posts})


def post_detail(request, pk):
    """Страница отдельной публикации."""
    post = get_object_or_404(
        Post.objects.filter(
            pub_date__lte=timezone.now(),
            is_published=True,
            category__is_published=True
        ),
        pk=pk
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    """Страница публикаций конкретной категории."""
    # Получаем активную категорию или 404
    category = get_object_or_404(Category, slug=category_slug,
                                 is_published=True)
    posts = Post.objects.filter(
        category=category,
        pub_date__lte=timezone.now(),
        is_published=True
    ).order_by('-pub_date')
    return render(request, 'blog/category.html', {'category': category,
                                                  'post_list': posts})
