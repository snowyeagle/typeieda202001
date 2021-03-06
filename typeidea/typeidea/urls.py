"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from blog.views import post_list, post_detail, PostDetailView

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from blog.views import (
    IndexView, CategoryView, TagView,
    PostDetailView,  SearchView, AuthorView
)
from comment.views import CommentView
from config.views import links, LinkListView
from typeidea.custom_site import custom_site
from .autocomplete import CategoryAutocomplete, TagAutocomplete

# 理解为一个路径（正则字符串）对应一个函数的映射
'''
urlpatterns = [
    url(r'^$', post_list, name='index'),  # 若用户访问博客首页，就把请求传递到post_list函数中
    url(r'^category/(?P<category_id>\d+)/$',
        post_list, name='category-list'),  # 文章分类列表页
    url(r'^tag/(?P<tag_id>\d+)/$', post_list, name='tag-list'),  # 文章标签列表页
    url(r'^post/(?P<post_id>\d+).html$',
        post_detail, name='post-detail'),  # w文章详情页
    url(r'^links/$', links, name='likes'),
    url(r'^super_admin/', admin.site.urls, name='super-admin'),  # 管理用户
    url(r'^admin/', custom_site.urls, name='admin'),  # 管理文章
]
'''
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^category/(?P<category_id>\d+)/$',
        CategoryView.as_view(), name='category-list'),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag-list'),
    url(r'^post/(?P<post_id>\d+).html$',
        PostDetailView.as_view(), name='post-detail'),
    url(r'^links/$', LinkListView.as_view(), name='links'),
    url(r'^super_admin/', admin.site.urls, name='super-admin'),
    url(r'^admin/', custom_site.urls, name='admin'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^author/(?P<owner_id>\d+)/$', AuthorView.as_view(), name='author'),
    url(r'^comment/$', CommentView.as_view(), name='comment'),
    url(r'^category-autocomplete/$', CategoryAutocomplete.as_view(),
        name='category-autocomplete'),
    url(r'^tag-autocomplete/$', TagAutocomplete.as_view(), name='tag-autocomplete'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
