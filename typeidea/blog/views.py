from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Post, Category, Tag
from config.models import SideBar


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
        'sidebars': SideBar.get_all(),
    }
    context.update(Category.get_navs())
    return render(request, 'blog/list.html', context=context)


# 直接获取category_id对象，显示该文章的详细信息
def post_detail(request, post_id=None):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None

    context = {
        'post': post,
        'sidebars': SideBar.get_all(),
    }
    # context.update(Category.is_nav())
    return render(request, 'blog/detail.html', context={'post': post})


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'


class PostListView(ListView):
    queryset = Post.latest_posts()
    paginate_by = 1
    context_object_name = 'post_list'
    template_name = 'blog/list.html'


# Create your views here.
