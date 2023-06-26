from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

# Create your views here.


def ItemsView(request):
    item = Items.objects.all().order_by('category')
    paginator = Paginator(item, 2)
    page_number = request.GET.get('page')
    get_page = paginator.get_page(page_number)
    total_page = get_page.paginator.num_pages

    context = {
        'get_page':get_page,
        'lastpage': total_page,
        'totalpagelist':[n+1 for n in range(total_page)]
    }

    return render(request, 'product.html', context)
