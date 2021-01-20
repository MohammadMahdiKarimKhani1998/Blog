import json

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView

from .models import Post, Comment, CommentLike, Category

User = get_user_model()


class Posts(LoginRequiredMixin, ListView):
    model = Post
    ordering = ['created_at']
    template_name = 'blog/posts.html'


class Categories(LoginRequiredMixin, DetailView):
    model = Category
    template_name = 'blog/category.html'


class SinglePost(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/single_post.html'


@csrf_exempt
def like_dislike(request):
    data = json.loads(request.body)
    user = request.user
    comment = Comment.objects.get(id=data['comment_id'])
    status = data['status']
    try:
        if user in comment.comment_likes['users']:
            comment_like = CommentLike.objects.get(comment=comment, user=user)
            comment_like.status = status
            comment_like.save()
            response = {'like_num': comment.like_count, 'dislike_num': comment.dislike_count,
                        "comment_id": comment.id}
            return HttpResponse(json.dumps(response), status=201)
        else:
            CommentLike.objects.create(status=status, user=user, comment=comment)
            response = {'like_num': comment.like_count, 'dislike_num': comment.dislike_count, "comment_id": comment.id}
            return HttpResponse(json.dumps(response), status=201)
    except:
        response = {"error": "error"}
        return HttpResponse(json.dumps(response), status=400)


@csrf_exempt
def comment_view(request):
    data = json.loads(request.body)
    user = request.user
    try:
        comment = Comment.objects.create(post=Post.objects.get(slug=data['post']), content=data['content'], author=user)
        response = {"content": comment.content, "created_at": str(comment.created_at),
                    "author": comment.author.get_full_name(), "comment_id": comment.id, 'like_num': comment.like_count,
                    'dislike_num': comment.dislike_count}
        return HttpResponse(json.dumps(response), status=201)
    except:
        response = {"error": "error"}
        return HttpResponse(json.dumps(response), status=400)
