from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
# from django.urls import reverse_lazy
# from django.views.generic import ListView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.models import User
from .forms import *


def index(request):
    template_name = 'posts/index.html'
    post = Posts.objects.all().order_by('-id')
    post_number = post.count()
    if post_number == 1:
        message = f"{post_number} post available : "
    elif post_number == 0 :
        message = "No one post available :"
    else:
        message = f'{post_number} posts availables:'
    paginator = Paginator(post, 3)  # Show 4 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'post': page_obj,
        'message': message,
    }
    return render(request, f'{template_name}', context)


def new_post(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    template_name = 'posts/new_post.html'
    if request.POST:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            messages.success(request, 'Blog added successfully')
            return redirect('posts:index')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, f'{template_name}', context)


def update_post(request, id):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    posts = Posts.objects.get(id=id)
    if request.POST:
        form = PostForm(request.POST, request.FILES, instance=posts)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog updated successfully')
            return redirect('posts:create_comment', id=posts.id)
    else:
        form = PostForm(instance=posts)

    context = {
        'form': form
    }
    template_name = 'posts/update_post.html'
    return render(request, f'{template_name}', context)


def delete_post(request, id) :
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    posts = Posts.objects.get(id = id)
    posts.delete()
    messages.warning(request,'Blog deleted successfully')
    return redirect('posts:index')


def search_post(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    template_name = 'posts/search_post.html'
    search = request.GET.get('search')
    if search != '':

        post = Posts.objects.filter(
            Q(title__icontains=search) | Q(content__icontains=search)
        ).order_by('-id')

        post_number = post.count()

        if post_number == 0:
            message = f'{post_number} Result Available'
        elif post_number == 1:
            message = f'{post_number} Result Available'
        else :
            message = f'{post_number} Results Availables'

        context = {
            'post': post,
            'search': search,
            'message': message
        }
        return render(request, f'{template_name}', context)

    return HttpResponse('<h2>Fill the research field</h2>')


def create_comment(request, id):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    owner = request.user
    posts = Posts.objects.get(id=id)
    all_comment_by_post = posts.comment_set.all().order_by('-created_add')
    nb_comment = all_comment_by_post.count()

    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            user_post_coment = form.save(commit=False)
            user_post_coment.owner = owner
            user_post_coment.post = posts
            user_post_coment.save()
            return redirect('posts:create_comment', id=posts.id)
    else:
        form = CommentForm()
    context = {
            'form': form,
            'post': posts,
            'comments': all_comment_by_post,
            'comment_number': nb_comment
        }
    template_name = 'posts/details.html'
    return render(request, f'{template_name}', context)


def update_comment(request, id):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    comment = Comment.objects.get(id=id)
    post = comment.post.id

    if request.POST:
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('posts:create_comment', id = post)
    else:
        form = CommentForm(instance=comment)
    context = {
            'form': form,
        }
    template_name = 'posts/update_comment.html'
    return render(request, f'{template_name}', context)


def delete_comment(request, id):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    comment = Comment.objects.get(id=id)
    comment_post = comment.post.id
    comment.delete()

    return redirect('posts:create_comment', id = comment_post)


# def details(request, id):
#     if not request.user.is_authenticated:
#         return redirect('accounts:login')
#     template_name = 'posts/details.html'
#     posts = Posts.objects.get(id=id)
#
#     context = {
#         'post' : posts
#     }
#     return render(request,f'{template_name}',context)


# class PostDeleteView(DeleteView):
#     model = Posts
#     template_name = "posts/delete_post.html"
#     success_url = reverse_lazy("posts:index")
#     def get_object(self, queryset=None):
#         return super().get_object(queryset)


# class PostListView(ListView):
#     context_object_name = "post"
#     queryset = Posts.objects.all().order_by('-id')
#     template_name = "posts/index.html"
#     paginate_by = 3


# class PostCreateView(LoginRequiredMixin, CreateView) :
#     model = Posts
#     fields = ['title', 'content', 'image']
#     template_name = 'posts/new_post.html'
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)
#     success_url = reverse_lazy('posts:index')


# class PostUpdateView(LoginRequiredMixin, UpdateView):
#     model = Posts
#     fields = ['title', 'content', 'image']
#     template_name = 'posts/update_post.html'
#     success_url = reverse_lazy('posts:index')
