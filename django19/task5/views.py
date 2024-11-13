from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post

# Create your views here.




def post_list(request):
    posts = Post.objects.all()
    items_per_page = request.GET.get('items_per_page')
    if not items_per_page:
        items_per_page = 5
    paginator = Paginator(posts, items_per_page)
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)
    return render(request, 'task5/post_list.html', {'page_posts': page_posts})