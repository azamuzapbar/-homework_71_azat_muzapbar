from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views.generic import CreateView
from posts.forms import PostForm
from posts.models import Post


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
