from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView
from posts.forms import PostForm
from posts.models import Post, Like


class LikeView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self, request, post_id):
        user = request.user
        post = Post.objects.get(id=post_id)
        current_likes = post.like_count
        liked = Like.objects.filter(user=user, post=post).count()
        if not liked:
            Like.objects.create(user=user, post=post)
            current_likes += 1
        else:
            Like.objects.filter(user=user, post=post).delete()
            current_likes -= 1
        post.like_count = current_likes
        post.save()
        return HttpResponseRedirect(reverse('index'))


class PostCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'post_create.html'
    model = Post
    form_class = PostForm
    success_message = 'Статья создана'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')
