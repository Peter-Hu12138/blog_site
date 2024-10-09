from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Post
from .forms import blog_form
from django.template.defaultfilters import slugify


# Create your views here.

def get_post(request: HttpRequest, slug):
    post = Post.objects.get(slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'post.html', context)


def blog_home(request: HttpRequest):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'authors': [post.authorid for post in posts],
    }
    return render(request, 'blog_home.html', context)


@login_required(login_url='login')
def blog_writing(request: HttpRequest):
    """
    Register a user and redirect to homepageif a form is valid; otherwise, direct the user to fill the form.
    """
    if request.method == "POST":
        form = blog_form(request.POST)
        if form.is_valid():
            blog_instance = Post(
                title=form.cleaned_data["title"],
                content=form.cleaned_data["content"],
                status=form.cleaned_data["status"],
                authorid=request.user,
                slug=slugify(form.cleaned_data["title"])
                                 )
            blog_instance.save()
            return HttpResponseRedirect("/blog/")

    else:
        form = blog_form()

    return render(request, "blog_writing.html", {"form": form})
