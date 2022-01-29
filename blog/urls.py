from django.urls import path
from . import views
<<<<<<< HEAD
from .views import BlogCreateView, BlogUpdateView
=======
from .views import BlogCreateView, ShowProfilePageView, CreateProfilePageView
>>>>>>> 67a74e8b2cee2fc317ce074a485801540a8e1eb2

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
<<<<<<< HEAD
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
=======
    path('user_profile/<int:pk>/', ShowProfilePageView.as_view(), name='user_profile'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_user_profile'),
>>>>>>> 67a74e8b2cee2fc317ce074a485801540a8e1eb2
]
