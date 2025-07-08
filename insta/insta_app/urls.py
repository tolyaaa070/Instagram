from tkinter.font import names

from django.urls import path , include
from .views import *
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet, basename='users')
router.register(r'follow', FollowViewSet, basename='follow')
router.register(r'post_like' , PostLIkeViewSet,basename='post_like')
router.register(r'comment' , CommentViewSet , basename='comment')
router.register(r'comment_like' , CommentLikeViewSet , basename='comment_like')
router.register(r'save' , SaveViewSet , basename='save')
router.register(r'save_item', SaveItemViewSet,basename='save_item')
router.register(r'story' , StoryViewSet , basename='story')


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('post/' , PostListViewSet.as_view() , name ='post' ),
    path('post/<int:pk>/', PostDetailViewSet.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', PostEditViewSet.as_view(), name='post_edit'),
    path('post/create/', PostCreateViewSet.as_view(), name='post_create')

]
