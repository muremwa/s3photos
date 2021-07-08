from django.urls import path

from . import views

app_name = 'photos'

urlpatterns = [
    # /photos/
    path('', views.AllPosts.as_view(), name='index'),

    # /photos/like-actions/34/
    path('like-actions/<int:post_pk>/', views.like_or_unlike, name='liker'),

    # /photos/upload/
    path('upload/', views.UploadImage.as_view(), name='upload'),

    # photos/api/index/
    path('api/index/', views.all_posts_api, name='api_index'),

    # photos/api/upload/
    path('api/upload/', views.upload_image_api, name='api_upload'),
]
