from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string


def index (request):
    # t=render_to_string('women/index.html')
    # return HttpResponse(t)
    return render(request,'women/index.html')

def about(request):
    return render(request, 'women/about.html')

def categories(request,cat_id):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>id: {cat_id}</p>')

def categories_by_slug(request,cat_slug):
    if request.POST:
        print(request.POST)
    return  HttpResponse(f'<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>')

def archive(request,year):

    if year==2025:
        return  redirect(index)

    if year==2033:
        return  redirect('home')

    if year==2055:
        return HttpResponsePermanentRedirect('/')

    if year==2066:
        return  HttpResponseRedirect('/')

    if year==2077:
        uri=reverse('cats',args=('misic',))
        return redirect(uri)

    if year==2088:
        return redirect('cats','music')

    if year==2000:
        return  redirect('/',permanent=True)

    # if year==2001:
    #     return redirect('/')


    if year>2024:
        raise Http404()
    if year<1000:
        return redirect('/')

    return  HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')

def page_not_found(request,exception):
    return HttpResponseNotFound(f'<h1>Страница не найдена</h1>')

