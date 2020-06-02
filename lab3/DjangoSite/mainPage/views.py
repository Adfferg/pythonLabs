from django.views.generic import View
from .forms import TagForm, UserForm, PostForm
from .utils import *


def index(request):
    posts = Post.objects.all().order_by("-date_pub")[:20]
    return render(request, 'mainPage/mainPage.html', context={'posts': posts})


def show_users(request):
    users = User.objects.all()
    return render(request, 'mainPage/users.html', context={'users': users})


def contacts(request):
    return render(request, 'mainPage/contacts.html', {'values': ['Все вопросы задавайте по телефону или по почте',
                                                                 '+375-29-855-64-49', 'maxrusak01@gmail.com']})


def registration(request):
    return render(request, 'mainPage/registration.html')


def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'mainPage/post_detail.html', context={'post': post})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'mainPage/list_of_tags.html', context={'tags': tags})


def users_posts(request, author):
    author_of_post = Users.objects.get(User_Name__iexact=author)
    return render(request, 'mainPage/user_posts.html', context={'author_of_post': author_of_post})


def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'mainPage/tag_detail.html', context={'tag': tag})


class PostCreate(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'mainPage/post_create.html', context={'form': form})

    def post(self, request):
        bound_form = PostForm(request.POST)
        if bound_form.is_valid():
            new_post = bound_form.save()
            us = Users.objects.get(User_Name__iexact=request.user)
            new_post.name_of_user.add(us)
            new_post = bound_form.save()
            return redirect(new_post)
        return render(request, 'mainPage/post_create.html', context={'form': bound_form})


class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'mainPage/tag_create.html', context={'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'mainPage/tag_create.html', context={'form': bound_form})


class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'mainPage/object_update.html'


class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'mainPage/object_update.html'


class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    template = 'mainPage/object_delete.html'
    template2 = 'tags_list_url'


class PostDelete(ObjectDeleteMixin, View):
    model = Post
    template = 'mainPage/object_delete.html'
    template2 = 'index'


class UserCreate(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'mainPage/registration.html', context={'form': form})

    def post(self, request):
        bound_form = UserForm(request.POST)
        if bound_form.is_valid() and not User.objects.filter(
                username__iexact=bound_form.cleaned_data['User_Name']).count() and not User.objects.filter(
            email__iexact=bound_form.cleaned_data['Email']).count():
            bound_form.save()
            posts = Post.objects.all()
            return render(request, 'mainPage/mainPage.html', context={'posts': posts})
        return render(request, 'mainPage/registration.html', context={'form': bound_form})
