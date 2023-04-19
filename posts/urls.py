from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from posts.views.base import IndexView

from posts.views.post_add import PostCreateView

from posts.views.post_detail import PostDetailView

from posts.views.comment_add import CommentCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('posts/add/', PostCreateView.as_view(), name='post_add'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/comment/create/', CommentCreateView.as_view(), name='comment_create'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)