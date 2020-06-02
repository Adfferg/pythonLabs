from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.show_users, name='show_users_url'),
    path('post/create/', views.PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', views.post_detail, name='post_detail_url'),
    path('tag/create', views.TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>', views.tag_detail, name='tag_detail_url'),
    path('tag/<str:slug>/update/', views.TagUpdate.as_view(), name='tag_update_url'),
    path('tag/<str:slug>/delete/', views.TagDelete.as_view(), name='tag_delete_url'),
    path('post/<str:slug>/update/', views.PostUpdate.as_view(), name='post_update_url'),
    path('post/<str:slug>/delete/', views.PostDelete.as_view(), name='post_delete_url'),
    path('posts/<str:author>/', views.users_posts, name='users_posts_url'),
    path('tags/', views.tags_list, name='tags_list_url'),
    path('contacts/', views.contacts, name='contacts'),
    path('registration/', views.UserCreate.as_view(), name='registration_url'),
    path('accounts/', include('django.contrib.auth.urls')),
]
