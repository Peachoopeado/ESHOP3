from django.shortcuts import render, get_object_or_404, redirect
from .models import MainPartner, MainPartnerImg

# Create your views here.
def open_main(request):
    partner = MainPartner.objects.all()
    partner_img = MainPartnerImg.objects.all()
    data = {
        'partner': partner,
        'partner_img': partner_img
    }
    return render(request, 'main/main_page.html', data)