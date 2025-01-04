from django.shortcuts import render
from news.models import news
from django.db.models import Q
from django.core.paginator import Paginator

def displayData(request):
# for pagination purposes
    newsData = news.objects.all()  #fetch all the news data 
    pagination=Paginator(newsData,2) #add data and tell how many want to display 
    page_number=request.GET.get('page') #get the page number
    no=pagination.get_page(page_number)

    # if request.method=="GET":
    #     st=request.GET.get("search")
    #     if st != None:
    #         no = news.objects.filter(title=st) 
    data = {
        'news': no
    }

    return render(request, 'news.html', data)

def newsDetails(request, slug):
    no = news.objects.get(news_slug=slug)
    data = {
        'news': no
    }
    return render(request, 'news-details.html', data)