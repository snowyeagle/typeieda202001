from django.shortcuts import render
from .models import Post, Category, Tag


# 分类与文章是1:N的关系，所以先获取tag对象，后获取category_id对象的列表，即可显示该类的所有文章
def post_list(request, category_id=None, tag_id=None):
    tag = None
    category = None

    if tag_id:  # 先获取tag对象-标签
        post_list, tag = Post.get_by_tag(tag_id)
    elif category_id:
        post_list, category = Post.get_by_category(category_id)
    else:
        post_list = Post.latest_posts()

    # 将字典context传给html页面
    context = {
        'category': category,
        'tag': tag,
        'post_list': post_list,
    }
    return render(request, 'blog/list.html', context=context)


# 直接获取category_id对象，显示该文章的详细信息
def post_detail(request, post_id=None):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None
    return render(request, 'blog/detail.html', context={'post': post})

# Create your views here.
