from django.shortcuts import render,get_list_or_404
from Blog.models import post, category
from django.core.paginator  import Paginator,EmptyPage
from django.http import Http404
from BlogProject.settings import web_site_name,web_site_slogan,web_site_url
# Create your views here.
def home(request):
    """Ana Sayfa"""
    db = post.objects.filter(is_active=True).order_by('?')[:6]
    last_db = post.objects.filter(is_active=True).order_by('-time')[:3]
    return render(request, 'home.html', {
        'db': db,
        'last_db':last_db,
        'web_site_name': web_site_name,
        'web_site_slogan': web_site_slogan
    })


def about(request):
    """ Hakkımda Sayfası """
    last_db = post.objects.filter(is_active=True).order_by('-time')[:3]
    return render(request, 'about.html', {
        'last_db': last_db,
        'web_site_name':web_site_name,
        'web_site_slogan':web_site_slogan,
    })


def contact(request):
    """ İletişim Sayfası """
    last_db = post.objects.filter(is_active=True).order_by('-time')[:3]
    return render(request, 'contact.html', {
        'last_db': last_db,
        'web_site_name': web_site_name,
        'web_site_slogan': web_site_slogan
    })


def blog(request):
    """ Blog yazıların listelendiği sayfa"""
    last_db = post.objects.filter(is_active=True).order_by('-time')[:3]
    db = post.objects.filter(is_active=True).order_by('-time')[:6]
    post_db = post.objects.filter(is_active=True)
    category_db = category.objects.all()
    pages = Paginator(post_db,5)

    return render(request, 'blog.html', {
        'last_db': last_db,
        'db': db,
        'pages': pages,
        'category_db': category_db,
        'web_site_name': web_site_name,
        'web_site_slogan': web_site_slogan,
    })

def page(request,id):
    """ Blog Sayfalaması """
    last_db = post.objects.filter(is_active=True).order_by('-time')[:3]
    post_db = post.objects.filter(is_active=True).order_by('-time')
    category_db = category.objects.all()
    pages = Paginator(post_db,5)
    try:
        db = pages.page(id)
    except EmptyPage:
        raise Http404()
    return render(request, 'page.html', {
        'last_db': last_db,
        'db': db,
        'pages': pages,
        'category_db': category_db,
        'web_site_name': web_site_name,
        'web_site_slogan': web_site_slogan
    })


def blog_details(request, slug):
    """ makale_details sayfası """
    last_db = post.objects.filter(is_active=True).order_by('-time')[:3]
    category_db = category.objects.all()
    db = post.objects.filter(seo_url=slug,is_active=True)
    for seo_info in db:
        title = seo_info.title
        description = seo_info.description
        keywords = seo_info.keywords
        image =  seo_info.image
    return render(request, 'blog_details.html', {
        'last_db': last_db,
        'db': get_list_or_404(db),
        'category_db': category_db,
        'web_site_name': web_site_name,
        'web_site_slogan': web_site_slogan,
        'web_site_url':web_site_url,
        'title':title,
        'description':description,
        'keywords':keywords,
        'image':image
    })


def category_view(request, category_names):
    """ category details sayfası """
    last_db = post.objects.filter(is_active=True).order_by('-time')[:3]
    category_db_list = category.objects.all()
    category_db = category.objects.filter(seo_url=category_names)
    post_db = post.objects.filter(category_list__seo_url=category_names,is_active=True).order_by('-time')
    pages = Paginator(post_db,5)
    for seo_info in category_db:
        title = seo_info.category_name
        description = seo_info.category_description
        keywords = seo_info.category_keywords
    return render(request, 'category.html', {
        'last_db': last_db,
        'category_db_list': category_db_list,
        'category_db': category_db,
        'post_db': get_list_or_404(post_db),
        'pages':pages,
        'category_names':category_names,
        'title': title,
        'description': description,
        'keywords': keywords,
        'web_site_name': web_site_name,
        'web_site_slogan': web_site_slogan
    })



def category_page(request, category_names,id):
    """ category details sayfası """
    last_db = post.objects.filter(is_active=True).order_by('-time')[:3]
    category_db_list = category.objects.all()
    category_db = category.objects.filter(seo_url=category_names)
    post_db = post.objects.filter(category_list__seo_url=category_names,is_active=True).order_by('-time')
    pages = Paginator(post_db,5)
    for seo_info in category_db:
        title = seo_info.category_name
        description = seo_info.category_description
        keywords = seo_info.category_keywords
    try:
        db = pages.page(id)
    except EmptyPage:
        raise Http404()
    return render(request, 'category_page.html', {
        'last_db': last_db,
        'category_db_list': category_db_list,
        'category_db': category_db,
        'post_db': db,
        'pages':pages,
        'category_names':category_names,
        'title': title,
        'description': description,
        'keywords': keywords,
        'web_site_name': web_site_name,
        'web_site_slogan': web_site_slogan
    })


def human(request):
    """ humans.txt"""

    return render(request, 'blog_templates/humans.html')


def robots(request):
    """robots.txt"""

    return render(request, 'blog_templates/robots.html')

def last_content(request):
    """ Alt taraf son yazılar """
    last_db = post.objects.filter(is_active=True).order_by('-time')[:3]
    return render(request,'blog_templates/last_content.html',{
        'last_db':last_db
    })
