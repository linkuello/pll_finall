from django.urls import path, include  # Добавьте include сюда
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("blog", views.blog, name="blog"),
    path("create", views.create, name="create"),
    path("increaselikes/<int:id>", views.increaselikes, name="increaselikes"),
    path("profile/<int:id>", views.profile, name="profile"),
    path("profile/edit/<int:id>", views.profileedit, name="profileedit"),
    path("post/<int:id>", views.post, name="post"),
    path("post/comment/<int:id>", views.savecomment, name="savecomment"),
    path("post/comment/delete/<int:id>", views.deletecomment, name="deletecomment"),
    path("post/edit/<int:id>", views.editpost, name="editpost"),
    path("post/delete/<int:id>", views.deletepost, name="deletepost"),
    path("contact", views.contact_us, name="contact"),

    # Страницы для авторизации через Google (Allauth будет использовать кастомные шаблоны)
    path('accounts/', include('allauth.urls')), 
]
