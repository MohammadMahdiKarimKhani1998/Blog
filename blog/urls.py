from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import api
from .views import Posts, Categories, SinglePost, like_dislike, comment_view


urlpatterns = [
    path('posts/', Posts.as_view(), name='posts'),
    path('category/<slug:slug>/', Categories.as_view(), name='categories'),
    path('post/<slug:slug>/', SinglePost.as_view(), name='post'),
    path('comment/', comment_view, name='comment'),
    path('like_dislike/', like_dislike, name='like_dislike'),
    path('serialize/posts/', api.PostList.as_view(), name='post_list'),
    path('serialize/posts/<int:pk>/', api.PostDetail.as_view(), name='post_detail'),
    path('users/', api.UserList.as_view()),
    path('users/<int:pk>/', api.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
