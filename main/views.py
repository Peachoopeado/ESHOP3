from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def open_main(request):
    return render(request, 'main/main_page.html')