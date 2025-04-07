from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from myapp.models import Post, Comment, Contact  
from .forms import PostForm

def dashboard_home(request):
    total_users = User.objects.count()
    total_posts = Post.objects.count()
    total_comments = Comment.objects.count()
    total_contacts = Contact.objects.count()

    context = {
        'total_users': total_users,
        'total_posts': total_posts,
        'total_comments': total_comments,
        'total_contacts': total_contacts,
    }

    return render(request, 'dashboard/home.html', context)


def is_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_admin)
def manage_users(request):
    users = User.objects.all().order_by('-date_joined')
    return render(request, 'dashboard/manage_users.html', {'users': users})


@login_required
@user_passes_test(is_admin)
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if user.is_superuser:
        messages.error(request, "Нельзя удалить администратора.")
    else:
        user.delete()
        messages.success(request, "Пользователь удалён.")
    return redirect('manage_users')

def manage_users(request):
    users = User.objects.all()  # Получаем всех пользователей
    return render(request, 'dashboard/manage_users.html', {'users': users})

# Управление постами
def manage_posts(request):
    posts = Post.objects.all()  # Получаем все посты
    return render(request, 'dashboard/manage_posts.html', {'posts': posts})

# Управление комментариями
def manage_comments(request):
    comments = Comment.objects.all()  # Получаем все комментарии
    return render(request, 'dashboard/manage_comments.html', {'comments': comments})

# Управление контактами
def manage_contacts(request):
    contacts = Contact.objects.all()  # Получаем все сообщения
    return render(request, 'dashboard/manage_contacts.html', {'contacts': contacts})


def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    
    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        return redirect('dashboard:manage_users')
    
    return render(request, 'dashboard/edit_user.html', {'user': user})

def edit_post(request, pk):
    post = get_object_or_404(Post, id=pk)  # Загружаем пост по pk
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()  # Сохраняем изменения
            return redirect('manage_posts')  # Перенаправление на страницу с постами
    else:
        form = PostForm(instance=post)  # Загружаем форму с данными текущего поста

    return render(request, 'dashboard/edit_post.html', {'form': form, 'post': post})

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('manage_posts') 