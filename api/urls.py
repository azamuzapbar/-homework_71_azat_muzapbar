from django.urls import include, path
from rest_framework import routers

from api.views import PostView, LikeView, CommentView

router = routers.DefaultRouter()
router.register('posts', PostView)
router.register('likes', LikeView)
router.register('comments', CommentView)

urlpatterns = [
    path('', include(router.urls)),
]
