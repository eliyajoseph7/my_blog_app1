from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, InfoSource, WordsOfWisdom, AboutMe, Experience
# Create your views here.

def index(request):
    post  = Post.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(post, 6)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'posts': posts})

def blog_home(request):
    post = Post.objects.all().order_by('-id')
    page = request.GET.get('page', 1)

    paginator = Paginator(post, 9)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/blog_home.html', {'posts': posts})

def blog_info(request, the_slug):
    obj = Post.objects.get(slug=the_slug)
    infoSources = InfoSource.objects.filter(post=obj.id)
    
    context = {
        'object': obj,
        'infoSources': infoSources
    }
    return render(request, 'blog/blog_details.html', context)

def emmanuel_tv(request):
    return render(request, 'emmanueltv/etv.html')


def words(request):
    wisdom = WordsOfWisdom.objects.all().order_by('-id')
    obje = Post.objects.all().order_by('-id')[:7]
    context = AboutMe.objects.get()
    page = request.GET.get('page', 1)

    paginator = Paginator(wisdom, 4)
    try:
        words = paginator.page(page)

    except PageNotAnInteger:
        words = paginator.page(1)
    except EmptyPage:
        words = paginator.page(paginator.num_pages)
    return render(request, 'blog/words.html', {'words': words, 'obje': obje, 'context': context})


def aboutMe(request):
    context = AboutMe.objects.get()
    experience = Experience.objects.all()
    return render(request, 'blog/aboutMe.html', {'context': context, 'experience': experience})    