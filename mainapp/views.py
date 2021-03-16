from django.shortcuts import render, get_object_or_404
from .models import Project, ProjectImage, Advert, Patner

#imaginary function to handle an uploaded file
# from somewhere import handle_upload_file

# Create your views here.

def index(request):
    the_posts = Project.objects.all()
    context = {
    'the_posts':the_posts,
    }
    return render(request, 'mainapp/index.html', context)



def details(request, id):
    post = get_object_or_404(Project, id=id)
    photos = ProjectImage.objects.filter(post=post)

    context = {
        'post':post,
        'photos':photos,
    }
    return render(request, 'mainapp/details.html', context)


def about(request):
    return render(request, 'mainapp/about.html')

def board(request):
    return render(request, 'mainapp/board.html')


def information(request):
    return render(request, 'mainapp/information.html')


def research(request):
    return render(request, 'mainapp/research.html')


def training(request):
    the_posts = Project.objects.all()
    context = {
    'the_posts':the_posts,
    }
    return render(request, 'mainapp/training.html', context)


def finance(request):
    return render(request, 'mainapp/finance.html')


def kenya(request):
    return render(request, 'mainapp/kenya.html')

def tanzania(request):
    return render(request, 'mainapp/tanzania.html')

def uganda(request):
    return render(request, 'mainapp/uganda.html')

def patner(request):
    patners = Patner.objects.all()
    context = {
    'patners':patners,
    }
    return render(request, 'mainapp/index.html', context)

def privacy(request):
    return render(request, 'mainapp/privacy_policy.html')

def advert(request):
    items = Advert.objects.all()
    context = {
    'items':items,
    }
    return render (request, 'mainapp/adverts.html', context)
