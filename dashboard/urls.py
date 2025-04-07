from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),

    # Управление пользователями
    path('manage/users/', views.manage_users, name='manage_users'),
    path('users/delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('users/edit/<int:pk>/', views.edit_user, name='edit_user'),
    path('manage/posts/edit/<int:pk>/', views.edit_post, name='edit_post'), 
    
    

    # Управление постами
    path('manage/posts/', views.manage_posts, name='manage_posts'),

    # Управление комментариями
    path('manage/comments/', views.manage_comments, name='manage_comments'),

    # Обратная связь
    path('manage/contacts/', views.manage_contacts, name='manage_contacts'),
    path('manage/posts/delete/<int:pk>/', views.delete_post, name='delete_post'), 

]
