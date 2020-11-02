from django.shortcuts import render
from . import models
import markdown
import pygments
# Create your views here.

def index(request):
    entries = models.Entry.objects.all()
    return render(request,'blog/index.html',locals())

def detail(request,blog_id):
    entry = models.Entry.objects.get(id=blog_id)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    entry.body = md.convert(entry.body)
    entry.toc = md.toc
    entry.increase_visiting()
    return render(request,'blog/detail.html',locals())
