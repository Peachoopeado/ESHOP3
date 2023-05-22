from django.shortcuts import render, get_object_or_404, redirect
from .models import MainPartner, MainPartnerImg, News, NewsImage
from django.views.generic import DetailView


# Create your views here.
def open_main(request):
    partner = MainPartner.objects.all()
    partner_img = MainPartnerImg.objects.all()
    news = News.objects.order_by('-created')[:3]
    news_img = NewsImage.objects.all()

    data = {
        'partner': partner,
        'partner_img': partner_img,
        'news': news,
        'news_img': news_img,
    }
    return render(request, 'main/main_page.html', data)


def news_list(request):
    news = News.objects.all()
    data = {
        'news': news
    }
    return render(request, 'main/news.html', data)


class NewsDetailView(DetailView):
    model = News
    template_name = 'main/details_view.html'
    context_object_name = 'new_post'
