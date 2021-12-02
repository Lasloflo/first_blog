from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm, RegisterUserForm, LoginUserForm

# Create your views here.

# class BlogListView(ListView):
#     model = Post
#
#     template_name = 'index.html'

menu = {'Blog': "home", }

def index(request):
    posts = Post.objects.all()[:5]
    comments = Comment.objects.all()
    
    return render(request, 'main/index.html', {"posts": posts, "menu": menu})


def show_post(request, post_id):

    # post = Post.objects.get(pk=post_id)
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post_id=post_id, is_active=True)
    all_comments_post = len(comments)  # число всех комментариев
    initial = {'post': post.pk}  # заносим в форму ключ к комментарию(скрытый "forms.HiddenInput")
    form_class = CommentForm  # создаемя объект CommentForm (не объект класса), которую будем потом редактировать по необходимости
    form = form_class(initial=initial)  # передаем словарь с НАЧАЛЬНЫМ значением id поста
    if request.method == 'POST':
        c_form = CommentForm(request.POST)  # проверяет на POST-запрос. и создается объект класса формы с введенными данными

        if c_form.is_valid():
            c_form.save()
            return redirect(post)  # использовали редирект и 'цель'- объект модели post - (необходим get_absolute_url(self))
        else:
            form = c_form  # данные не валидны на странице отобразится форма с некорректно введенными данными

    data = {
        'post': post,
        'menu': menu,
        'commentform': form,
        'comments': comments,
        'all_comm': all_comments_post,
    }
    return render(request, 'main/blog_post.html', data)

class RegisterUser(CreateView):  # класс для создания пользователя. Регистрация
    form_class = RegisterUserForm  # форма регистрации пльзователся
    template_name = 'main/register.html' # шаблон в котором будет форма
    success_url = reverse_lazy('login')  # переход на страницу после регистрации

    def get_context_data(self, *, object_list=None, **kwargs):  # стандартный метод класса для передачи контекста в шаблон
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form):  # метод вызывается при успешной регистрации польщователя
        user = form.save()   # сохраняем форму в БД. Добавляем пользователя в БД
        login(self.request, user)  # функция login автоматически авторизовывает пользователя
        return redirect('home')  # перенаправляет на страницу 'home' почле удачной регистрации


# def login(request):
#     pass

class LoginUser(LoginView):  # класс наследуется от стандартного класса LoginView - в котором прописана логика АУТОНТИФИКАЦИИ
    # form_class = AuthenticationForm  # стандартная форма для аутонтификации пользователя
    form_class = LoginUserForm  # пользовательская форма для аутонтификации пользователя
    template_name = 'main/login.html'  # путь к шаблону нобработк формы входа

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Вход на сайт'
        return context

    def get_success_url(self):  # фукция определяет на какую страницу перейдет пользователь после удачной регистрации
        return reverse_lazy('home')
    #  это же можно прописать в settings.py
    #  как LOGIN_REDIRECT_URL = '/'   - перенаправление на домашнюю страницу

def logout_user(request):  # функция для выхода
    logout(request)  # стандартный метод для выхода пользователя
    return redirect('login')